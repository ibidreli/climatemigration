"""
Erzeugt die aktuelle Causal Loop Map und Stakeholder Map aus den Originalkarten (v1) in archiv/.

Die Originalkarten bleiben unverändert. Dieses Skript übernimmt sie 1:1 und
wendet nur die Änderungen aus 02_LE1_Review.md an (Kennzeichnung A1, A2, ..., D2).
Causal Loop Map: Teil 02 (Detailmodule) bleibt unverändert.
Stakeholder Map: alle bestehenden Inhalte bleiben unverändert, ergänzt wird
unten der Abschnitt «Einfluss und Betroffenheit» (D2).

Ausgabe:
    drawio/causal_loop_map.drawio, causal_loop_map.png
    drawio/stakeholder_map.drawio, stakeholder_map.png

Aufruf:
    python generate_maps.py

Benötigt Pillow. Schrift: Arial (Windows), sonst Liberation Sans / DejaVu Sans.
"""
from pathlib import Path
import copy
import math
import re
import xml.etree.ElementTree as E
from PIL import Image, ImageDraw, ImageFont

HIER = Path(__file__).resolve().parent
LE1 = HIER.parent
ARCHIV = LE1 / 'archiv'

FARBEN = {'green': ('#d5e8d4', '#82b366'), 'blue': ('#dae8fc', '#6c8ebf'), 'red': ('#f8cecc', '#b85450'),
          'yellow': ('#fff2cc', '#d6b656'), 'purple': ('#e1d5e7', '#9673a6'), 'grey': ('#f5f5f5', '#888888')}


# ---------------------------------------------------------------------------
# Hilfsfunktionen für das drawio-XML
# ---------------------------------------------------------------------------

def style_dict(style):
    d = {}
    for teil in (style or '').strip(';').split(';'):
        if '=' in teil:
            k, v = teil.split('=', 1)
            d[k] = v
    return d


def style_str(d):
    return ''.join(f'{k}={v};' for k, v in d.items())


class Karte:
    def __init__(self, pfad):
        self.baum = E.parse(pfad)
        self.root = self.baum.getroot().find('.//root')

    def zelle(self, id):
        for c in self.root.iter('mxCell'):
            if c.get('id') == id:
                return c
        raise KeyError(id)

    def pruefe_neu(self, id):
        if any(c.get('id') == id for c in self.root.iter('mxCell')):
            raise ValueError(f'ID {id} existiert bereits')

    def entferne(self, id):
        self.root.remove(self.zelle(id))

    def text(self, id, wert):
        self.zelle(id).set('value', wert)

    def geometrie(self, id, x=None, y=None, w=None, h=None):
        g = self.zelle(id).find('mxGeometry')
        for k, v in (('x', x), ('y', y), ('width', w), ('height', h)):
            if v is not None:
                g.set(k, str(v))

    def farbe(self, id, name):
        c = self.zelle(id)
        s = style_dict(c.get('style'))
        s['fillColor'], s['strokeColor'] = FARBEN[name]
        c.set('style', style_str(s))

    def kante_stil(self, id, **aenderungen):
        c = self.zelle(id)
        s = style_dict(c.get('style'))
        s.update({k: str(v) for k, v in aenderungen.items()})
        c.set('style', style_str(s))

    def knoten(self, id, text, x, y, farbe, vorlage='water', w=300, h=105):
        """Neuer Knoten im Stil eines bestehenden Kernmodell-Knotens."""
        self.pruefe_neu(id)
        neu = copy.deepcopy(self.zelle(vorlage))
        neu.set('id', id)
        neu.set('value', text)
        self.root.append(neu)
        self.geometrie(id, x, y, w, h)
        self.farbe(id, farbe)

    def beschriftung(self, id, text, x, y, w, h, vorlage='b'):
        """Neue Schleifenbeschriftung im Stil der bestehenden B-Beschriftung."""
        self.pruefe_neu(id)
        neu = copy.deepcopy(self.zelle(vorlage))
        neu.set('id', id)
        neu.set('value', text)
        self.root.append(neu)
        self.geometrie(id, x, y, w, h)

    def kante(self, id, quelle, ziel, label, vorlage, exit=None, entry=None, punkte=None, label_pos=None, **stil):
        """Neue Kante im Stil einer bestehenden Kante."""
        self.pruefe_neu(id)
        neu = copy.deepcopy(self.zelle(vorlage))
        neu.set('id', id)
        neu.set('source', quelle)
        neu.set('target', ziel)
        neu.set('value', label)
        g = neu.find('mxGeometry')
        for a in g.findall('Array'):
            g.remove(a)
        if label_pos is not None:
            g.set('x', str(label_pos))  # drawio: Position der Beschriftung entlang der Kante (-1 bis 1)
        if punkte:
            arr = E.SubElement(g, 'Array', attrib={'as': 'points'})
            for px, py in punkte:
                E.SubElement(arr, 'mxPoint', x=str(px), y=str(py))
        self.root.append(neu)
        s = style_dict(neu.get('style'))
        if exit:
            s['exitX'], s['exitY'] = map(str, exit)
        if entry:
            s['entryX'], s['entryY'] = map(str, entry)
        s.update({k: str(v) for k, v in stil.items()})
        neu.set('style', style_str(s))

    def neue_zelle(self, id, vorlage, text, x, y, w, h, **stil):
        """Neue Zelle als Kopie einer bestehenden, mit eigenem Text, Ort und Stil."""
        self.pruefe_neu(id)
        neu = copy.deepcopy(self.zelle(vorlage))
        neu.set('id', id)
        neu.set('value', text)
        self.root.append(neu)
        self.geometrie(id, x, y, w, h)
        st = style_dict(neu.get('style'))
        st.update({k: str(v) for k, v in stil.items()})
        neu.set('style', style_str(st))

    def seitenhoehe(self, h):
        self.baum.getroot().find('.//mxGraphModel').set('pageHeight', str(h))

    def speichern(self, pfad):
        E.indent(self.baum)
        self.baum.write(pfad, encoding='utf-8', xml_declaration=True)


# ---------------------------------------------------------------------------
# Änderungen gegenüber dem Original (siehe 02_LE1_Review.md)
# ---------------------------------------------------------------------------

def aenderungen(k):
    rot, lila, grau = FARBEN['red'][1], FARBEN['purple'][1], FARBEN['grey'][1]

    # A1: Dürre entfernen, nur Niederschlag als Klimatreiber
    k.entferne('e2')
    k.entferne('drought')

    # A9: exogene Grösse grau
    k.farbe('rain', 'grey')
    k.kante_stil('e1', strokeColor=grau, fontColor=grau)

    # A2: Kette Ertrag -> Produktion -> Einkommen statt Ertrag -> Einkommen
    k.entferne('e4')
    k.kante('v2_e1', 'yield', 'production', '+', 'e3', exit=(.8, 1), entry=(0, .5), punkte=[(1170, 862)])

    # A7: Abwanderung wirkt über die Bevölkerung auf die Arbeitskräfte
    k.entferne('e7')
    k.kante('v2_e2', 'pop', 'labor', '+', 'e8', exit=(0, 1), entry=(1, 0), label_pos=0.6)
    k.kante_stil('e6', strokeColor=rot, fontColor=rot)

    # A4, A5, A8: Abgewanderte Personen, Rücküberweisungen über den Bestand, Netzwerk-Schleife R2
    k.knoten('v2_emigrants', 'Abgewanderte\nPersonen', 2760, 300, 'purple', w=270, h=90)
    k.entferne('e10')
    k.kante('v2_e3', 'migration', 'v2_emigrants', '+', 'e11', exit=(1, .1), entry=(0, .5))
    k.kante('v2_e4', 'v2_emigrants', 'remit', '+ ||', 'e11', exit=(.2, 0), entry=(1, .8))
    k.kante('v2_e5', 'v2_emigrants', 'migration', '+ ||', 'e11', exit=(0, .9), entry=(1, .3))

    # A6: Schleife B1 schliessen (Name wie im Detailmodul «Bevölkerung und Abwanderung»)
    k.knoten('v2_food', 'Nahrungsmittel-\nverfügbarkeit pro Person', 2420, 690, 'blue')
    k.kante('v2_e6', 'pop', 'v2_food', '−', 'e6', exit=(.5, 1), entry=(.5, 0), strokeColor=grau, fontColor=grau)
    k.kante('v2_e7', 'v2_food', 'migration', '−', 'e6', exit=(0, .5), entry=(1, 1), label_pos=-0.6, strokeColor=grau, fontColor=grau)

    # A10, B3: Schleifen benennen, R1 als Hypothese kennzeichnen
    k.text('r', 'R1 · VERSTÄRKEND\nArbeitskräfte–Einkommen\n(Hypothese)')
    k.geometrie('r', y=630, h=110)
    k.text('b', 'B2 · AUSGLEICHEND\nRücküberweisungen\n(möglich)')
    k.beschriftung('v2_r2', 'R2 · VERSTÄRKEND\nNetzwerk', 2760, 420, 270, 60)
    k.beschriftung('v2_b1', 'B1 · AUSGLEICHEND\nVersorgung', 2760, 800, 270, 60)

    # Legende und Fusszeile an die neuen Schleifen anpassen
    k.text('key', '+  Gleiche Wirkungsrichtung\n−  Entgegengesetzte Wirkungsrichtung\n||  Verzögerung\nGrau: exogen (wirkt von aussen)\n\nVorzeichen gelten bei sonst gleichen Bedingungen.\nSie bedeuten nicht «gut» oder «schlecht».')
    k.geometrie('key', y=760, h=260)
    k.text('corefoot', 'R: gerade Anzahl negativer Verbindungen → verstärkend.    B: ungerade Anzahl → ausgleichend.\nDie mögliche B2-Schleife wird nur bei geeigneter Datenlage und angemessener Modellkomplexität übernommen.')


def aenderungen_stakeholder(k):
    """D2: Einordnung der Akteure nach Einfluss und Betroffenheit (eigene Einschätzung)."""
    y0 = 2740
    k.neue_zelle('v2_power_title', 'rel-title', 'EINFLUSS UND BETROFFENHEIT', 50, y0, 3000, 60)
    k.neue_zelle('v2_power_sub', 'rel11note',
                 'Eigene Einschätzung: Wer kann das System beeinflussen, und wer trägt die Folgen? '
                 'Grundlage für die Massnahmen-Szenarien in LE4.', 50, y0 + 60, 3000, 45, fontSize=22)
    # Spaltenköpfe (Betroffenheit) und Zeilenköpfe (Einfluss)
    k.neue_zelle('v2_col_hoch', 'rel-title', 'Betroffenheit hoch', 300, y0 + 120, 1350, 45, fontSize=24)
    k.neue_zelle('v2_col_tief', 'rel-title', 'Betroffenheit tief bis mittel', 1700, y0 + 120, 1350, 45, fontSize=24)
    k.neue_zelle('v2_row_hoch', 'rel-title', 'Einfluss hoch bis mittel', 50, y0 + 180, 230, 260, fontSize=24)
    k.neue_zelle('v2_row_tief', 'rel-title', 'Einfluss tief', 50, y0 + 460, 230, 260, fontSize=24)
    felder = [
        ('v2_q1', 'Eng einbinden\n\nAbwandernde Personen · Lokale Gemeinschaften', 300, y0 + 180, 'yellow'),
        ('v2_q2', 'Für Massnahmen gewinnen (LE4)\n\nNationale Regierung · Lokale und regionale Behörden\n'
                  'Hilfs- und Entwicklungsorganisationen · Landwirtschaftliche Beratungsstellen', 1700, y0 + 180, 'orange'),
        ('v2_q3', 'Schützen und informieren\n\nLokale Haushalte · Landwirtschaftliche Betriebe und Bauern\n'
                  'Zurückbleibende Familien', 300, y0 + 460, 'red'),
        ('v2_q4', 'Informieren\n\nForschung und internationale Organisationen', 1700, y0 + 460, 'grey'),
    ]
    fuell = dict(FARBEN, orange=('#ffe6cc', '#d79b00'))
    for id, text, x, y, farbe in felder:
        k.neue_zelle(id, 'rel0', text, x, y, 1350, 260, fontSize=24,
                     fillColor=fuell[farbe][0], strokeColor=fuell[farbe][1])
    k.seitenhoehe(3500)


# ---------------------------------------------------------------------------
# PNG zeichnen (vereinfachte Darstellung der drawio-Datei)
# ---------------------------------------------------------------------------

def schrift(size, bold=False):
    kandidaten = (['C:/Windows/Fonts/arialbd.ttf', '/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf',
                   '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'] if bold else
                  ['C:/Windows/Fonts/arial.ttf', '/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf',
                   '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'])
    for pfad in kandidaten:
        try:
            return ImageFont.truetype(pfad, size)
        except OSError:
            pass
    return ImageFont.load_default()


def farbwert(v, standard):
    if not v or v == 'none':
        return None
    m = re.match(r'light-dark\(([^,]+),', v)
    return m.group(1) if m else (v or standard)


def zeichne_png(drawio, png, rand=40):
    root = E.parse(drawio).getroot().find('.//root')
    zellen = list(root.iter('mxCell'))
    knoten = {}
    for c in zellen:
        if c.get('vertex') == '1':
            g = c.find('mxGeometry')
            knoten[c.get('id')] = tuple(float(g.get(a)) for a in ('x', 'y', 'width', 'height'))
    x0 = min(v[0] for v in knoten.values()) - rand
    y0 = min(v[1] for v in knoten.values()) - rand
    x1 = max(v[0] + v[2] for v in knoten.values()) + rand
    y1 = max(v[1] + v[3] for v in knoten.values()) + rand
    im = Image.new('RGB', (int(x1 - x0), int(y1 - y0)), 'white')
    d = ImageDraw.Draw(im)
    T = lambda x, y: (x - x0, y - y0)

    for c in zellen:
        if c.get('vertex') != '1':
            continue
        s = style_dict(c.get('style'))
        x, y, w, h = knoten[c.get('id')]
        fuell = farbwert(s.get('fillColor'), '#ffffff')
        rahmen = farbwert(s.get('strokeColor'), '#000000')
        if fuell or rahmen:
            d.rounded_rectangle((*T(x, y), *T(x + w, y + h)), radius=16, fill=fuell, outline=rahmen, width=2)
        text = c.get('value') or ''
        if not text:
            continue
        size = int(s.get('fontSize', 20))
        f = schrift(size, s.get('fontStyle') == '1')
        zeilen = []
        for absatz in text.split('\n'):
            zeile = ''
            for wort in absatz.split():
                test = (zeile + ' ' + wort).strip()
                if d.textlength(test, font=f) > w - 36 and zeile:
                    zeilen.append(zeile)
                    zeile = wort
                else:
                    zeile = test
            zeilen.append(zeile)
        lh = size + 7
        yy = y + (h - len(zeilen) * lh) / 2
        for z in zeilen:
            xx = x + 18 if s.get('align') == 'left' else x + (w - d.textlength(z, font=f)) / 2
            d.text(T(xx, yy), z, fill='#263238', font=f)
            yy += lh

    for c in zellen:
        if c.get('edge') != '1':
            continue
        s = style_dict(c.get('style'))
        farbe = s.get('strokeColor', '#888888')
        sx, sy, sw, sh = knoten[c.get('source')]
        tx, ty, tw, th = knoten[c.get('target')]
        punkte = [(float(p.get('x')), float(p.get('y'))) for p in c.find('mxGeometry').iter('mxPoint')]
        ps = [(sx + float(s.get('exitX', .5)) * sw, sy + float(s.get('exitY', .5)) * sh)] + punkte + \
             [(tx + float(s.get('entryX', .5)) * tw, ty + float(s.get('entryY', .5)) * th)]
        ps = [T(*p) for p in ps]
        for p, q in zip(ps, ps[1:]):
            if s.get('dashed') == '1':
                laenge = math.dist(p, q)
                for t in range(0, int(laenge), 20):
                    u, v = t / laenge, min(t + 11, laenge) / laenge
                    d.line((p[0] + (q[0] - p[0]) * u, p[1] + (q[1] - p[1]) * u,
                            p[0] + (q[0] - p[0]) * v, p[1] + (q[1] - p[1]) * v), fill=farbe, width=3)
            else:
                d.line((p, q), fill=farbe, width=3)
        if s.get('endArrow', 'block') != 'none':
            p, q = ps[-2:]
            a = math.atan2(q[1] - p[1], q[0] - p[0])
            d.polygon([q, (q[0] - 16 * math.cos(a - .4), q[1] - 16 * math.sin(a - .4)),
                       (q[0] - 16 * math.cos(a + .4), q[1] - 16 * math.sin(a + .4))], fill=farbe)
        label = c.get('value')
        if label:
            # Beschriftung in der Mitte des Pfads
            laengen = [math.dist(p, q) for p, q in zip(ps, ps[1:])]
            pos = float(c.find('mxGeometry').get('x', 0))
            rest = sum(laengen) * (0.5 + pos / 2)
            for (p, q), l in zip(zip(ps, ps[1:]), laengen):
                if rest <= l:
                    lx, ly = p[0] + (q[0] - p[0]) * rest / l, p[1] + (q[1] - p[1]) * rest / l
                    break
                rest -= l
            f = schrift(23, True)
            bw = d.textlength(label, font=f)
            d.rectangle((lx - bw / 2 - 5, ly - 17, lx + bw / 2 + 5, ly + 17), fill='white')
            d.text((lx - bw / 2, ly - 14), label, fill=farbe, font=f)
    im.save(png)


if __name__ == '__main__':
    for name, aendern in (('causal_loop_map', aenderungen), ('stakeholder_map', aenderungen_stakeholder)):
        karte = Karte(ARCHIV / f'{name}_v1.drawio')
        aendern(karte)
        drawio = HIER / f'{name}.drawio'
        png = LE1 / f'{name}.png'
        karte.speichern(drawio)
        zeichne_png(drawio, png)
        print('geschrieben:', drawio.name, png.name)
