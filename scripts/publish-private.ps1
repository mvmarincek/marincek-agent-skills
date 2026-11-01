# Explicit confirmation required, does not run automatically.
$ErrorActionPreference = 'Stop'
Set-Location (Split-Path -Parent $PSScriptRoot)
Write-Host 'This will create a PRIVATE GitHub repository mvmarincek/agent-skills and push the current directory.'
Write-Host 'Review files and git status before confirming. Do NOT run inside an existing unrelated repository.'
$answer = Read-Host 'Type PUBLISH-PRIVATE to continue'
if ($answer -cne 'PUBLISH-PRIVATE') { Write-Host 'Cancelled.'; exit 0 }
if (-not (Get-Command git -ErrorAction SilentlyContinue)) { throw 'Git CLI is required' }
if (-not (Get-Command gh -ErrorAction SilentlyContinue)) { throw 'GitHub CLI is required' }
gh auth status
if ($LASTEXITCODE -ne 0) { throw 'Authenticate GitHub CLI first: gh auth login' }
if (Test-Path '.git') { throw 'A .git repository already exists; review manually to avoid overwriting remotes.' }
gh repo view mvmarincek/agent-skills --json name *> $null
if ($LASTEXITCODE -eq 0) { throw 'Repository already exists; use a manual PR workflow.' }
python scripts/validate.py
if ($LASTEXITCODE -ne 0) { throw 'Skill validation failed.' }
git init -b main
git add .
git commit -m 'feat: initialize private agent skills knowledge base'
if ($LASTEXITCODE -ne 0) { throw 'Git commit failed; configure your git user.name/email.' }
gh repo create mvmarincek/agent-skills --private --source . --remote origin --push
if ($LASTEXITCODE -ne 0) { throw 'GitHub CLI publish failed; inspect git status/remotes before retrying.' }
Write-Host 'Published to https://github.com/mvmarincek/agent-skills'
