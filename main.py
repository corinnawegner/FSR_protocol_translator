import deepl
import os

DEEPL_AUTH_KEY = "a6da2cc8-76a5-40e4-8a2c-fe08b7aa288c:fx"
translator = deepl.Translator(DEEPL_AUTH_KEY)


def read_german_protocol():
    pass


def split_text_by_signal_word(text, signal_word="TOP"):
    chunks = text.split(signal_word)
    return chunks


def translate_chunk(text):
    result = translator.translate_text(text, target_lang="EN-US")
    return result.text

def reassemble_text(chunks):
    protocol_translated = ''.join(chunks)
    return protocol_translated

def write_document():
    pass

def main_function(protocol_german):
    chunks_german = split_text_by_signal_word(protocol_german, "TOP")
    chunks_translated = []
    for i in range(len(chunks_german)):
        chunk_translated = translate_chunk(chunks_german[i])
        chunks_translated.append(chunk_translated)
    print(chunks_translated)
    protocol_translated = reassemble_text(chunks_translated)
    return protocol_translated


text_test = """
Protokoll der Fachschaftsratssitzung vom 30.05.2024
Legende
Beschluss (Ja, Nein, Enthaltungen)
Meinungsbild (Ja, Nein)
Aufgabe
Anwesende
FSR
Tim N., Vincent R., Johanna, Ive, Jannis F., David, Josie, Janna, Elisa, Leif, Ole M., Corinna, Oskar

Gäste
Protokollantinnen
Josie und Corinna

Tagesordnung
Protokoll der letzten Sitzung
Finanzen
Aktuelles
Schulung bei Frau Lux
Sprechstunde
Zusammenlegung Hausmeisterteams
Stand Studiwerk CaPhy-Angebot
Gremien-Vernetzung
ZaPF Orga Auftakttreffen
Torte verbindet
MINT-Lehramtsstammtisch
AK-Berichte
Park zwischen Physik und Chemie
Flinta* Nudelabend
Physik und Ethik
Hamster
Bericht Jour Fixe
Bericht Sondersitzung LSV Stufenlehramt
Bericht Zielereinbarungsgespräch
ZaPF-Bericht
Verschiedenes
Awareness Infektionsrisiko in Vorlesungen
AK Protokolle
Semesterabschlussparty
Maiball 2025 Location
Regal für den FSRR
Glutenfreies Angebot in der Mensa?
Vorschlag Lehrpreis
Mehr Vernetzung mit anderen FSen ?
Verleih von FSR-Material an nicht-FSR/nicht-studi Sachen
Beginn: 18:20 Uhr
xx:xx Uhr: xxx kommt/geht

TOP 1: Protokoll der letzten Sitzung
Anmerkungen: Beim FSRV Bericht stimmte das Abstimmungsergebnis nicht genau, statt einstimmig gab es eine Enthaltung. Das wird geändert.
18:21 Uhr: Oskar kommt
TOP 3 Aktuelles: ein Satz (Gasthörerin in der Fakultät) stand ohne Kontext da, der Kontext ist ein Hinweis von Frau Lux. Wird ergänzt.

Abstimmung: Soll das Protokoll so veröffentlicht werden? Angenommen (9,0,4)

TOP 2: Finanzen
Wir haben noch keinen Haushalt, also keine Finanzen.

TOP 3: Aktuelles
Schulung bei Frau Lux
Nicolai wird für einige Zeit keine FSR Arbeit leisten, sodass das gesamte Soziales Team wegfällt. Die Aufgaben werden aufgeteilt. Deshalb müssten wir eine Schulung bei Frau Lux (innerhalb der nächsten drei Monate) machen, an einem Freitag Vormittag.
Die Organisation (Doodle und Kommunikation mit Frau Lux) übernimmt Ole.

Sprechstunde
Nicolai fehlt und daher muss jemand die Sprechstunde machen. Fine übernimmt die Koordination, aber nicht immer die Sprechstunde. Sie hat den Schlüssel. Ole und Elli machen die Sprechstunde zusammen mit Fine.

Zusammenlegung Hausmeisterteams
Fine war bei den Hausmeistern und hat nachgefragt was die Zusammenlegung bedeutet. Hier eine Zusammenfassung, gerne so in der Sitzung vorlesen

Die Hausmeisterteams von Physik, Geo und Chemie werden zusammengelegt. Dadurch wird Personal eingespart, eine Stelle an der Chemie fällt weg, aber bei uns bleiben (erstmal) alle erhalten. Was sich ändert ist, wann die Hausmeister da und für uns erreichbar sind. Bis 15 Uhr ändert sich nichts. In der Spätschicht wird sich abgewechselt, sodass in manchen Wochen dann niemand in der Physik vor Ort ist. Dann muss man im Zweifel anrufen, wenn man etwas braucht. Die Person, die Schicht hat, kommt dann nur abends zum Abschließen rüber. Generell sind die Hausmeister abends nicht mehr wie bisher bis 10 da, sondern gehen früher (wann genau wurde sich nicht gemerkt, könnte man nochmal fragen, nicht später als 8 auf jeden Fall).

Stand Studiwerk CaPhy-Angebot
Im Stupa wurde der Studiwerk-Studi-Vorsitz gewählt. Was wurde aus der Email mit der Caphy? Nichts.
Janna hat mal angerufen, die Antwort war genau so unkonkret wie in der Mail.

Vorschlag: Studis im Vorsitz kontaktieren und versuchen da Einfluss zu nehmen
Janna tut das (per Mail). Mailadresse kommt von Vincent.

Gremien-Vernetzung
Das Gremiengrillen hat stattgefunden! Es waren viele Menschen da.

Feedback von den Profs, dass es häufiger stattfinden sollte. Menschen im Allgemeinen befürworten das Öffnen der Veranstaltung für mehr Gremien (oder auch alle Ehrenamtsinhabende).

Wir wollen das weiter im Blick haben und nicht vergessen

ZaPF Orga Auftakttreffen
Wir haben den Rückhalt von Ralph, Montag wird es nochim JF angesprochen. Das Auftakttreffen zum Beginn der Planung soll bald stattfinden, eintragen im Doodle für die Terminabspreche. Auch außerhalb des FSR dürfen Menschen mitmachen! Die einfach zum Treffen mitbringen. jDPG wird auch explizit eingeladen, sobald der Termin steht. Fragen an Tim.

Torte verbindet
Samstag Nachmittag wird ein Einkauf aus der SB Union verwertet. Erdbeer Sahne Torte, Gutenbergstraße 12.

MINT Lehramtsstammtisch
War mittelmäßg besucht. Aber die Anwesenden hatten eine gute Zeit.

Quantenjahr
Am 04.06. um 10:30 gibt es das Auftakttreffen im Auditorium. Eine Erinnerung an die "angemeldeten" Menschen gehen raus.

TOP 4: AK-Berichte
Park zwischen Physik und Chemie
Die rechtlichen Regelungen wurden geklärt. Niemand weiß, warum es da überhaupt einen Parkplatz gibt. Das weitere Vorgehen lautet reden mit Menschen: 1. JF 2. Chemie 3. Campusübergreifend. Im Gremienvernetzungstreffen kam raus, dass die Profs Bock haben. Frey redet mit dem Dekanat der Chemie, wir mit ihren Studis. Jippie!

18:36 Uhr: Mica kommt

FLINTA-Nudelabend
Der Nudelabend wird mit Pesto stattfinden. Der Raum ist SR14, Emails und Werbetexte wurden geschrieben. 18.06. um 18:15 findet das statt. Plakate gibt es schon.
Elli und Josie kochen Nudeln.

Physik und Ethik
Es wird wieder stattfinden! Eine Person wurde angeschrieben, bei der anderen gibts keine Mailadresse, deshalb wird jetzt Tim H.s Linkedin genutzt. Es wird um Physik in Göttingen während der Zeit des dritten Reichs gehen. Das ganze findet erst im November (oder so) statt.
Es wird einen Folge AK geben.

Hamster
Es waren 3 Leute da, nur einer konnte LaTeX lokal installieren, dort konnte man aber nicht kompilieren. Aber das Repo funktionniert wieder für andere Leute, immerhin. Da wird sich später drum gekümert.

TOP 5: Bericht Jour Fixe
Im letzten Jour fixe gab es eine Diskussion zu Workload im Studium. Martin wollte wissen, wo das Studium im internationalen Vergleich da stehen soll. Da gab es ein Missverständnis zwischen Martin und uns.
Von uns angesprochen wurden die Zettelabgaben, insbesondere deren Staffelung und Änderung ihrer Abgabezeiten weg von 08:00.
Uns ist wichtig, dass nicht durch schwierige Aufgaben versucht wird, die "Elite" übrig zu behalten, um uns im internationalen Vergleich zu pushen.

Hust-Nies-Etikette: Unsicherheit ob das in die Mail kommen soll, weil es eigentlich selbstverständlich ist. Schauen wir mal, ob ne Mail kommt. Problem wird aber generell anerkannt.

TOP 7: Bericht Sondersitzung LSV Stufenlehramt
Ive war in einer Sondersitzung der LSV in der über das Stufenlehramt informiert und diskutiert wurde.
In einigen Bundesländern gibt es das schon, in Niedersachsen haben sich für das Stufenlehramt als Pilotprojekt alle Unis bis auf Vechta und Oldenburg beworben.
Es gibt auf Landesebene verschiedene AG's die sich mit z.B. mit der Studienstruktur auseinandergesetzt haben und den Rahmen setzen aber die genaue Creditverteilung plant die Uni, mit die größte Änderung ist die Einführung eines Praxissemesters mit 15 C im Master statt zwei Fachpraktika.
Auch seitens der Zewil gibt es noch keine endgültige Version der Creditverteilung auf die Module bzw. auf die verschiedenen Bereiche des Lehramtsstudiums.
Die ZEWIL hat 10 Leitplanken ausgearbeitet, die den Fächern als Empfehlung dienen und einen Rahmen zu geben z.B. wie Vor- und Nachbereitung im Praktikum aussehen sollte und was zu berücksichtigen ist z.B. das Studierende von Fremdsprachen einen verpflichtenden Auslandsaufenthalt haben.
Insgesamt birgt das Stufenlehramt viele Chancen aber auch einige Herausforderungen hinsichtlich der Planung, da das Studium quasi grundlegend umstrukturiert wird.
Da die EntscheidungsträgerInnen wie z.B. die studentischen VertreterInnen in den StuKos oft nicht aus dem Lehramt sind möchte sich die LSV mit ihnen vernetzen und sie informieren und unterstützen in all den Fragen, die das Stufenlehramt aufwirft.

TOP 8: Bericht Zielereinbarungsgespräch
Der Vizepräsident für Studium und Lehre, sowie Profs und das SDekanat waren dabei. Wir hatten viele Punkte mit baulichen Maßnahmen, weil Ammer da viel unterstützt hat und wir auf diesem Weg die (fast) barrierefreie Tür bekommen haben.
Wadetzky meint, es wär nicht seine Baustelle (pun intended).
Das liegt wohl daran, dass Ammer sich für unsere Tür+Weg sehr stark einsetzten musste.

18:54 Uhr: Feueralarm im Gebäude, aber nur im 2. Stock, lol, wir bleiben einfach sitzen.

Das SDekanat ist ein bisschen frustiert mit der Zentrale, weil von da viele Versuche abgeblockt werden, Sachen besser zu machen.

Wir wurden darauf angesprochen, dass unsere Frauenquote sehr niedrig ist, auch im deutschlandweiten Vergleich mit anderen Physik-Fakultäten. Martin meint, das liegt an Parkstudierenden. Vereinbartes Ziel: Wir denken mal an Frauen.

Niemand mag EXA, niemand weiß wieso es kam, UniVZ war viel geiler.

Der Nordcampus fühlt sich etwas vergessen. Aber nicht verzagen, es fließt auch Geld in den Nordcampus, wir sehen es nur nicht! Friede, Freude, Eierkuchen.

Nächstes Mal: Mehr auf studienrelevante Dinge fokussieren

TOP 9: ZaPF-Bericht
Wird angehangen. Hier nur Diskussionen.

19:03 Burger sind endlich da, kurze Pause bis 19:10
Eine Stellungnahme zur Antidiskriminierungspolitik in unserer Uni wird mit in den FakRat genommen.

Viele Unis haben keine Prüfungsan- und Abmeldung
Warum gibt es hier eine Prüfungsanmeldung? Für die Raumplanung, und um zu wissen wie viel Papiere gedruckt werden. An anderen Unis klappt das aber auch ohne Abmeldefristen.
Was wollen wir für uns daraus ziehen? Erstmal keine konkreten, weil wir uns auf die Diskussion zu unbegrenzten Prüfungsversuchen fokussieren wollen.

Klausuren duerfen bei der Einsicht immer abfotografiert werden
Wir wollen das unter den Profs bekannt machen mit Belegen

Diskussion: Offene Tutorien, wo ein Tutor mit SHK Stelle den Leuten die kommen helfen bei ihren Hausaufgaben
Wir wollen beim S-Dekanat fordern, dass die Saaluebungen umstrukturiert werden (mehr Eigenarbeit und Unterstuetzung statt vorrechnen)

Praktika: Es gibt keine vernuenftige Statistikausbildung vor den Praktika
Wir wollen, dass uns die Versuche besser angeleitet werden (nicht ins kalte Wasser geworfen werden z.B. bei Laserstrahljustierung, sondern Techniken dazu lernen wie man es richtig macht)

4-Jahres Bachelor: Wir wollen Guidelines verfassen, was man machen kann, um den Erstis zu Helfen

20:16 Uhr: Mica geht

Wollen wir mehr Werbung fuer Physik an den Schulen machen?
Es gibt schon StudienbotschafterInnen, also ist es nicht unsere Aufgabe
Wir koennen aber das Amt des Studienbotschafters mehr bewerben

20:26 kurze Pause
20:42 weiter

TOP 10: Verschiedenes
Wo ist Vorkurs-Tutorenwerbung?
Keiner weiss was, wird im JF gefragt

AK Protokolle
Es wurde mal so gemacht, dass es erwartet wird, AK Protokolle zu lesen, damit die Berichte knapper sind.

Konsens:
Menschen, die einen wichtigen AK geleitet haben, könnten dem Sprecherteam Bescheid geben, dass entsprechende Protokolle gelesen werden sollen. Dann kann diese Info in der Ladung übermittelt werden.
(Sprecherteam in diesem Kontext: Johanna, die Ladende.)

Semesterabschlussparty
Wir haben bisher noch keine Planung, weil dieser Vincent J. nicht mehr da ist.
Wollen wir eine organisieren? (Fine würde beraten!)
David würde mitmachen. Semesterabschlussparty wäre in ca. zwei Monaten, und die Orga sollte entsprechend bald anfangen. Menschen bis nächste Woche Donnerstag Zeit, sich zu überlegen, ob sie mitmachen wollen.

21:11 Katha geht

Maiball 2025 Location
Die Stadthalle und das Bürgerhaus Bovenden wurden angefragt.
Bürgerhaus Bovenden hat noch nicht geantwortet.
Für den 10.05. ist die Stadthalle jetzt reserviert, wir müssen Anfang nächster Woche Bescheid geben, ob wir das da machen wollen.
Kosten: Dieses Jahr 1500€, Stadthalle mind. 3000€ für 10h.
Es passen bei Bankettbestuhlung 412 Personen rein. Rechteckige Tische und Tanzfläche.
Personalkosten: Sicherheitsdiensteinsatzleiter, Brandsicherheitswache
Musikboxen sind teuer.
Aber hey, Mikrofone sind billig!
Macht summasumarum nach Adam Riese (und Elisa): mind. 5000€

Vincent kann das besser einschätzen (eigene Aussage). Er sagt: Nö, jibbet nich.

Die Menschen, die den nächsten Winterball organisieren, haben aus Kostengründen nicht die Stadthalle gemietet.

Jetzt noch angeschrieben werden soll irgendein Haus (Johanna und Jannis wissen, welches). Da brauchen wir noch die Mailadresse. Es gibt einen alten Tanzsaal in Rosdorf.

Regal für den FSRR
Hier wieder Input von Fine, anschließende Fragen und Diskussion müsst ihr selbst protokollieren (:

Die Monitorfüße sind weg (yay!, danke Janna), dadurch ist im Keller mehr Platz. Es gibt den Plan, einen der Schränke aus dem FSRR runter zu räumen um dort für den Spieleabend sinnvoll Spiele lagern zu können. Dadurch entsteht wiederum Platz im FSRR. Den brauchen wir zur Zeit vor allem, um unsere Taschen/Rucksäcke besser zu lagern. Deshalb gibt es den Vorschlag ein Regal von Kleinanzeigen zu holen, das dann neben der Garderobe stehen kann.
Man könnte sowas grundsätzlich aus unseren Geldern bezahlen, aber wir könnten es auch über die Pfandkasse bezahlen.

Es gibt Diskussionen und verschiedene Meinungen dazu, ob die Spiele in den Keller verlagert werden sollen. Argumente: Spieleabend-Menschen müssen viel laufen. Wenn wir was ausleihen, müssten sonst Menschen, die die Spiele ausgeben, in den Keller laufen. Potentiell könnten wir vielleicht stattdessen andere Dinge runter verlegen (z.B. den ganz linken?)
Man könnte es auch testweise ausprobieren.

Verfahren: Der Aufräum-AK wird höher priorisiert, und wir machen da mal Inventur, und schauen ob was besseres in den Keller könnte.

ToDo: Handywecker mit Erinnerung zur Evaluierung @Corinna

Glutenfreies Angebot in der Mensa?
Menschen bonden über ihre FreundInnen mit Glutenintoleranz.

Das Umsetzen von einem glutenfreien Angebot in Mensen könnte schwer sein. Anfragen können wir ja trotzdem, vielleicht macht sich wenigstens jemand Gedanken drum?
Kreuzkontaminationen sind ein wichtiger Punkt.
Nett wäre z.B. in Cafeterien ein Angebot an glutenfreiem Gebäck, das kann man einzeln abgepackt kaufen!

Vorschlag Lehrpreis
Vor ner Weile (14.05.) kam eine Mail zum ars Legendi Preis.
Es gibt die Überlegung, Matthias Krüger vorzuschlagen. Er müsste dafür eine Stellungnahme schreiben, die Fakultät und der FSR auch.
Bevor wir mit ihm direkt sprechen, fragen wir Yvonne, um zu vermeiden, dass dann am Ende wer dagegen ist, nachdem wir schon Versprechungen gemacht haben. Es wird im JF abgeklärt, falls nötig dann im FakRat.

Wir schlagen Matthias Krüger für den ars Legendi Preis vor (für die Theorie II) (12,0,0)

Mehr Vernetzung mit anderen FSen?
Es gibt den Vorschlag für mehr Vernetzung mit anderen FSen. Bspw. sowas wie gemeinsam Pizza essen.
Es wird angemerkt, dass es einen Nordcampus Stammtisch. Bei dem Vorschlag geht es jedoch mehr um ein eins zu eins Treffen mit anderen FSen und auch nicht nur vom Nordcampus sondern auch vom Z-Campus.

FSRV-Antrag-Time! Corinna schreibt einen Antrag.
Es gibt viel Zustimmung, Menschen werden unterstützen.

Verleih von FSR-Material an nicht-FSR/nicht-studi Sachen
Kellnerweg und RSC wollen unsere Bierbänke ausleihen.
Der RSC hat gar keine Connection zu Studis, der Kellnerweg arguably schon, aber man hat keine explizit Verantwortlichen, die in der Physik ansässig sind.

Meinungen: Wir sind enttäuscht von den Geos, weil drei Tische nicht zurückkamen, und andere dreckig/beschädigt waren. Deshalb wollen wir ein bisschen vorsichtig sein. Man könnte über einen Pfand nachdenken. Z.B. 10-20€ pro Garnitur. Dann muss es auch einen Wisch geben, wo von Ausleihenden unterschrieben wird, wie viele Garnituren sie ausgeliehen haben.

Wir erheben einen Pfand für die Ausleihe unserer Bierzeltgarnituren für externe (nicht Institut Physik) Ausleihende, dabei sind 20€ pro Garnitur angesetzt, davon 10€ pro Tisch und 5€ je Bank
(13,0,0)

Fachschaftszeitung
Niemeyer hat auf dem Gremiengrillen begeistert von seiner Fachschaftszeitung erzählt und in Nostalgie geschwelgt. Fanden wir ganz cool. Das Ding sollte einmal im Semester kommen und sowohl Infos als auch Spaß beinhalten. Müsste man sich drum kümmern, können aber auch gut Leute von außerhalb machen. Und es können Memes rein! Außerdem Interviews mit Profs, Erklärungen zu Gremien und Politik.
Grob gesagt: Schülerzeitung.

Stadtradeln
Startet am 01.06., vielleicht haben ja Leute Bock, Yvonne ist auch dabei.

Ende: 22:02 Uhr
"""

result = main_function(text_test)
print(result)
