#!/usr/bin/env python3
"""
Vantage Weekly Public Signal Sweep — Minimal Viable Version
"""

import json
from datetime import datetime
from pathlib import Path

def load_sources():
    sources_path = Path(__file__).parent / "sources.json"
    with open(sources_path, "r") as f:
        data = json.load(f)
    return data["sources"]

def run_sweep(sources):
    print(f"\n{'='*60}")
    print(f"VANTAGE WEEKLY SWEEP STARTED — {datetime.now().isoformat()}")
    print(f"{'='*60}\n")
    
    print(f"Loaded {len(sources)} public sources from registry\n")
    
    for source in sources:
        print(f"[{source['priority'].upper()}] {source['name']}")
        print(f"  URL: {source['url']}")
        print(f"  Signals: {', '.join(source['signal_types'])}")
        print(f"  Automation: {source['automation_readiness']}")
        if source['automation_readiness'] == 'high':
            print(f"  → Would call Grok-4.3 for structured extraction\n")
        else:
            print(f"  → Would use browse_page monitoring\n")
    
    print(f"\n{'='*60}")
    print("SWEEP COMPLETE — In production this will:")
    print("  1. Call Grok/Claude for each high-priority source")
    print("  2. Extract structured events (funding, formations, hires...)")
    print("  3. Write to Supabase with confidence scores")
    print("  4. Send summary to Slack/email")
    print(f"{'='*60}\n")

if __name__ == "__main__":
    sources = load_sources()
    run_sweep(sources)
    print("✅ First successful sweep completed. Ready for production expansion.")

