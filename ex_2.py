timp = input("Introduceți timpul în formatul 00:00 AM/PM: ")
timp_con = timp.lower()

if timp_con.count('pm'):
    timp = timp.replace("pm", "")
    ore, minute = timp.split(':')
    ore = int(ore)
    if ore != 12:
        ore += 12

elif timp_con.count('am'):
    timp = timp.replace('am', '')  # eliminăm AM

print( f"{ore}:{minute}")
