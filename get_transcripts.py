from supadata import Supadata

client = Supadata(api_key="sd_43b3927fd46663fe73f1a6bec50e1307")

videos = [
    {
        "url": "https://www.youtube.com/watch?v=O-bo48WTDfg",
        "filename": "april-dunford-positioning.md",
        "title": "April Dunford - Positioning Talk"
    },
    {
        "url": "https://www.youtube.com/watch?v=Zndx-XeoP0U",
        "filename": "dave-gerhardt-b2b-ad-campaigns.md",
        "title": "Dave Gerhardt - B2B Ad Campaigns That Actually Worked"
    }
]

for video in videos:
    try:
        transcript = client.youtube.transcript(video["url"])
        content = f"# {video['title']}\n## Source: {video['url']}\n\n"
        for item in transcript.content:
            content += item.text + " "
        
        with open(f"research/youtube-transcripts/{video['filename']}", "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Successfully saved: {video['filename']}")
    except Exception as e:
        print(f"Error for {video['filename']}: {e}")

print("Done!")