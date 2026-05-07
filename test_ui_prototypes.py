#!/usr/bin/env python3

import json
from ai_agent import AIWriter

# Test different theme combinations
test_cases = [
    {"title": "Neural Health Tracker", "themes": ["Kesehatan", "Neural"]},
    {"title": "Rhythm Game", "themes": ["Game", "Ritme"]},
    {"title": "AI Music Composer", "themes": ["AI", "Musik"]},
    {"title": "IoT Productivity Hub", "themes": ["IoT", "Produktivitas"]},
    {"title": "Health App", "themes": ["Kesehatan"]},
    {"title": "Game Hub", "themes": ["Game"]},
    {"title": "Music Player", "themes": ["Musik"]},
    {"title": "AI Assistant", "themes": ["AI"]},
    {"title": "IoT Dashboard", "themes": ["IoT"]},
    {"title": "Generic App", "themes": ["Data", "Horor", "VR"]}
]

print("Testing UI Prototype Generation for Different Theme Combinations:")
print("=" * 70)

for i, test_case in enumerate(test_cases, 1):
    print(f"\n{i}. {test_case['title']}")
    print(f"   Themes: {', '.join(test_case['themes'])}")

    # Generate UI prototype
    ui_html = AIWriter.generate_ui_prototype({
        "title": test_case["title"],
        "themes": test_case["themes"]
    })

    # Check which UI type was generated
    if "Neural Health" in ui_html and "meditation" in ui_html.lower():
        ui_type = "🧠 Neural Health Tracker"
    elif "Rhythm Game" in ui_html and "rhythm-btn" in ui_html:
        ui_type = "🎵 Rhythm Game"
    elif "AI Music Composer" in ui_html and "piano" in ui_html.lower():
        ui_type = "🎼 AI Music Composer"
    elif "IoT Productivity Hub" in ui_html and "device-card" in ui_html:
        ui_type = "🔗 IoT Productivity Hub"
    elif "Health Tracker" in ui_html and "metric-card" in ui_html:
        ui_type = "🏥 Health Tracker"
    elif "Game Hub" in ui_html and "game-card" in ui_html:
        ui_type = "🎮 Game Hub"
    elif "Music Player" in ui_html and "album-art" in ui_html:
        ui_type = "🎵 Music Player"
    elif "AI Assistant" in ui_html and "chat-container" in ui_html:
        ui_type = "🤖 AI Assistant"
    elif "IoT Dashboard" in ui_html and "sensor-card" in ui_html:
        ui_type = "🔗 IoT Dashboard"
    else:
        ui_type = "📱 Generic UI"

    print(f"   Generated UI: {ui_type}")

    # Save to file for inspection
    filename = f"test_ui_{i}_{test_case['title'].replace(' ', '_').lower()}.html"
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(ui_html)
    print(f"   Saved to: {filename}")

print("\n" + "=" * 70)
print("✅ UI Prototype generation test completed!")
print("📁 Check the generated HTML files to see different UI layouts.")