#!/usr/bin/env node

"use strict";

const fs = require("fs");
const path = require("path");
const os = require("os");
const { spawnSync } = require("child_process");

const PKG_ROOT = path.resolve(__dirname, "..");
const SKILL_SLUG = "seed-audio-1-0";
const PKG_JSON = JSON.parse(fs.readFileSync(path.join(PKG_ROOT, "package.json"), "utf8"));

function printHelp() {
  console.log(`Seed Audio 1.0 Skill Installer v${PKG_JSON.version}

Usage:
  npx evolink-seed-audio                 interactive installer
  npx evolink-seed-audio -y              non-interactive installer
  npx evolink-seed-audio --yes           non-interactive installer
  npx evolink-seed-audio -y --path <dir> install to a specific skills directory
  npx evolink-seed-audio --llms          print agent installation guide
  npx evolink-seed-audio --skill         print SKILL.md
  npx evolink-seed-audio --version       print version
  npx evolink-seed-audio --help          show help
`);
}

function readFile(rel) {
  process.stdout.write(fs.readFileSync(path.join(PKG_ROOT, rel), "utf8"));
}

function expandHome(p) {
  return p.replace(/^~/, os.homedir());
}

function defaultSkillsDir() {
  const home = os.homedir();
  const candidates = [
    path.join(home, ".openclaw", "skills"),
    path.join(home, ".claude", "skills"),
    path.join(home, ".opencode", "skills")
  ];
  for (const candidate of candidates) {
    if (fs.existsSync(candidate)) return candidate;
  }
  return path.join(home, ".openclaw", "skills");
}

function copyDir(src, dest) {
  if (!fs.existsSync(src)) return;
  fs.mkdirSync(dest, { recursive: true });
  fs.cpSync(src, dest, { recursive: true });
}

function copyFile(rel, destDir) {
  const src = path.join(PKG_ROOT, rel);
  if (!fs.existsSync(src)) return;
  const dest = path.join(destDir, rel);
  fs.mkdirSync(path.dirname(dest), { recursive: true });
  fs.copyFileSync(src, dest);
}

function commandExists(cmd) {
  const result = spawnSync(os.platform() === "win32" ? "where" : "which", [cmd], {
    stdio: "ignore"
  });
  return result.status === 0;
}

function install(targetPath) {
  const skillsDir = expandHome(targetPath || defaultSkillsDir());
  const dest = path.join(skillsDir, SKILL_SLUG);
  fs.mkdirSync(dest, { recursive: true });

  for (const file of ["SKILL.md", "llms-install.md", "_meta.json", "LICENSE"]) {
    copyFile(file, dest);
  }
  for (const dir of ["scripts", "references", "docs", "examples"]) {
    copyDir(path.join(PKG_ROOT, dir), path.join(dest, dir));
  }

  const missing = ["curl", "python3"].filter((cmd) => !commandExists(cmd));
  console.log(`Installed ${SKILL_SLUG} to ${dest}`);
  if (missing.length) {
    console.log(`Missing optional dependencies: ${missing.join(", ")}`);
  }
  if (!process.env.EVOLINK_API_KEY) {
    console.log("Set EVOLINK_API_KEY before generating audio.");
  }
}

const args = process.argv.slice(2);
if (args.includes("--help") || args.includes("-h")) {
  printHelp();
  process.exit(0);
}
if (args.includes("--version")) {
  console.log(PKG_JSON.version);
  process.exit(0);
}
if (args.includes("--llms")) {
  readFile("llms-install.md");
  process.exit(0);
}
if (args.includes("--skill")) {
  readFile("SKILL.md");
  process.exit(0);
}

let targetPath = null;
const pathIndex = args.indexOf("--path");
if (pathIndex !== -1 && args[pathIndex + 1]) {
  targetPath = args[pathIndex + 1];
}

install(targetPath);
