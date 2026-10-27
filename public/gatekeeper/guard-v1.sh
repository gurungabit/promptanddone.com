#!/bin/bash
# v1: deny any tool call that mentions .env
if cat | grep -q '\.env'; then
  jq -n '{hookSpecificOutput:{hookEventName:"PreToolUse",permissionDecision:"deny",permissionDecisionReason:"Blocked: .env is off limits"}}'
fi
