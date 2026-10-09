#!/usr/bin/env python3
"""Refresh a small, curated Wikipedia football knowledge cache for GitHub Pages."""
import json, time, urllib.parse, urllib.request
from datetime import datetime, timezone
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/"data"/"wiki-cache.json"
TITLES=["Lionel Messi","Cristiano Ronaldo","Kylian Mbappé","Erling Haaland","Neymar","Kevin De Bruyne","Mohamed Salah","Luka Modrić","Real Madrid CF","FC Barcelona","Manchester United F.C.","Liverpool F.C.","Manchester City F.C.","FC Bayern Munich","Juventus FC","Arsenal F.C.","FIFA World Cup","UEFA Champions League","Premier League","Vietnam national football team"]
def fetch(title):
 params={"action":"query","format":"json","origin":"*","prop":"pageimages|extracts","piprop":"thumbnail","pithumbsize":"320","exintro":"1","explaintext":"1","exsentences":"4","redirects":"1","titles":title}
 url="https://en.wikipedia.org/w/api.php?"+urllib.parse.urlencode(params)
 req=urllib.request.Request(url,headers={"User-Agent":"FootballUniverseEducationalDemo/1.0 (GitHub Actions knowledge cache)"})
 with urllib.request.urlopen(req,timeout=20) as response: payload=json.load(response)
 for page in payload.get("query",{}).get("pages",{}).values():
  if "missing" in page:return None
  return {"title":page.get("title",title),"extract":page.get("extract",""),"thumbnail":page.get("thumbnail",{}).get("source",""),"url":"https://en.wikipedia.org/?curid="+str(page.get("pageid","")),"pageid":page.get("pageid")}
 return None
def main():
 entries=[]
 for title in TITLES:
  try:
   item=fetch(title)
   if item and item.get("title"):entries.append(item)
   time.sleep(0.35)
  except Exception as exc: print(f"Warning: could not fetch {title}: {exc}")
 data={"updatedAt":datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC"),"source":"Wikipedia / MediaWiki Action API","sourceUrl":"https://www.mediawiki.org/wiki/API:Main_page","entries":entries}
 OUT.parent.mkdir(parents=True,exist_ok=True);OUT.write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding="utf-8")
 print(f"Wrote {len(entries)} entries to {OUT}")
if __name__=="__main__":main()
