import subprocess, json, re, sys, concurrent.futures as cf
pairs = [("strawberry","r"),("raspberry","r"),("blueberry","r"),("mississippi","s"),("bookkeeper","e"),("committee","m"),("assassinate","s"),("occurrence","c"),("embarrassment","r"),("onomatopoeia","o"),
("necessary","s"),("parallel","l"),("hippopotamus","p"),("accommodation","m"),("cinnamon","n"),("banana","a"),("rhinoceros","r"),("successfully","s"),("Connecticut","c"),("Massachusetts","s"),
("antidisestablishmentarianism","i"),("supercalifragilisticexpialidocious","i"),("floccinaucinihilipilification","i"),("pneumonoultramicroscopicsilicovolcanoconiosis","o"),("electroencephalography","e"),
("uncharacteristically","c"),("incomprehensibilities","i"),("counterrevolutionaries","r"),("Llanfairpwllgwyngyll","l"),("deoxyribonucleic","e"),
("zucchini","z"),("quizzical","z"),("xylophone","x"),("jazz","z"),("syzygy","y"),("rhythm","h"),("Mississippi","p"),("queue","u"),("pizzazz","z"),("knickknack","k")]
models=["haiku","sonnet"]
def ask(m,w,l,mode):
    if mode=="plain": p=f"How many times does the letter {l} appear in the word \"{w}\"? Answer with just the number."
    else: p=f"How many times does the letter {l} appear in the word \"{w}\"? First spell the word out letter by letter, then count. End with a final line 'ANSWER: <number>'."
    for _ in range(3):
        r=subprocess.run(["claude","-p","--model",m,"--tools","","--disable-slash-commands","--no-session-persistence","--output-format","json",p],capture_output=True,text=True)
        try:
            j=json.loads(r.stdout); out=j["result"]; cost=j["total_cost_usd"]; mu=list(j["modelUsage"])[0]; break
        except Exception as e: out="";cost=0;mu="?"
    nums=re.findall(r"ANSWER:\s*(\d+)",out) if mode!="plain" else re.findall(r"\d+",out)
    got=int(nums[-1]) if nums else None
    true=w.lower().count(l)
    return dict(model=m,mode=mode,word=w,letter=l,true=true,got=got,ok=got==true,cost=cost,mu=mu,out=out[:600])
jobs=[(m,w,l,mode) for m in models for mode in("plain","spell") for (w,l) in pairs for _ in range(2)]
with cf.ThreadPoolExecutor(8) as ex: res=list(ex.map(lambda a:ask(*a),jobs))
json.dump(res,open("results.json","w"),indent=1)
for m in models:
  for mode in("plain","spell"):
    s=[r for r in res if r["model"]==m and r["mode"]==mode]; print(m,mode,sum(r["ok"] for r in s),len(s))
print("cost",sum(r["cost"] for r in res))
