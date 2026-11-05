# Honorářová kalkulačka kameramana (AČK)

Webová kalkulačka, která počítá honorář kameramana zvlášť za **přípravu, natáčení a postprodukci** a ukazuje, kolik vychází na jeden odpracovaný den.

Výchozí denní sazby jsou mediány z dotazníku Asociace českých kameramanů (AČK) z května 2024 (36 respondentů). Jde o sazby, které kameramani považují za přiměřené, nikoli o průměr skutečně vyplácených honorářů. Kalkulačka není závazný sazebník.

## Co umí

- 7 typů projektů (film, seriál, sekvenční natáčení, přenos, hodinový dokument, dva typy dokumentárních cyklů) s důstojnou a minimální sazbou podle průzkumu
- příprava a postprodukce jako počet dní × procento denní sazby; **minimum je 50 %**, nižší hodnotu aplikace nepřijme, vyšší ano
- návrh počtu přípravných dní (1,2 dne na natáčecí den)
- příplatek za švenkování, když si hlavní kameraman švenkuje sám
- přesčasy, noční dny, víkendy a svátky, cestovní dny
- srovnání s nabízeným paušálem a přepočet paušálu na den
- odvozené sazby štábu (švenkr 62,5 %, ostřič 40 %, 2. asistent 30 %)
- DPH 21 % pro plátce
- kopírování souhrnu, sdílitelný odkaz s vyplněnými hodnotami, tisk

Vše běží v prohlížeči, nic se neodesílá. Aplikace je jediný soubor `index.html` bez závislostí (kromě písma Archivo z Google Fonts).

## Zveřejnění na GitHub Pages

1. Nahrajte `index.html` a `README.md` do repozitáře (např. `ack-kalkulacka`).
2. V repozitáři otevřete **Settings → Pages**.
3. V části *Build and deployment* zvolte **Deploy from a branch**, větev `main` a složku `/ (root)`.
4. Po minutě bude kalkulačka na `https://<uživatel>.github.io/<repozitář>/`.

## Úprava sazeb

Minimum pro přípravu a postprodukci je v `index.html` v konstantě `MIN_PCT`, sazby z průzkumu v poli `CATS`, výchozí procenta příplatků v objektu `DEFAULTS` a podíly štábu v poli `CREW`. Výše příplatků za noc, víkend, přesčasy a cestovní dny je zatím návrh k diskusi v AČK.
