#!/bin/bash
# v2: also deny hidden-file globs, command substitution, base64 and printf tricks
ARGS=$(jq -r '.tool_input | .command // .file_path // .pattern // .path // ""')
if echo "$ARGS" | grep -Eq '\.env|\.[e*?[]|\$\(|`|base64|printf'; then
  jq -n '{hookSpecificOutput:{hookEventName:"PreToolUse",permissionDecision:"deny",permissionDecisionReason:"Blocked: dotfile access is off limits"}}'
fi
