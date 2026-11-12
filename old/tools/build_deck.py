"""VOLSHi pitch deck generator. Dark/gold slides, projection voice: systems are
presented as working. No hedging."""

from reportlab.lib.pagesizes import landscape, A4
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor

W, H = 960, 540  # 16:9 widescreen
BG = HexColor("#0B0B0D")
GOLD = HexColor("#C9A84C")
WHITE = HexColor("#F5F2ED")
MUTED = HexColor("#9a958c")
DIM = HexColor("#5c594f")

OUT = "/home/hatch/workspace/website/assets/volshi-pitch-deck.pdf"


def slide(draw):
    c = canvas.Canvas(OUT, pagesize=(W, H))
    c.setTitle("VOLSHi — Pitch Deck")
    c.setAuthor("VOLSHi")
    for fn in SLIDES:
        c.setFillColor(BG)
        c.rect(0, 0, W, H, fill=1, stroke=0)
        fn(c)
        # footer
        c.setFillColor(DIM)
        c.setFont("Helvetica", 7)
        c.drawString(40, 28, "VOLSHi")
        c.drawRightString(W - 40, 28, "volshi.com")
        c.showPage()
    c.save()
    print("wrote", OUT)


def title(c, text, y=None, size=34):
    y = y or H - 150
    c.setFillColor(WHITE)
    c.setFont("Helvetica-Bold", size)
    c.drawCentredString(W / 2, y, text)


def kicker(c, text, y=None):
    y = y or H - 90
    c.setFillColor(GOLD)
    c.setFont("Helvetica", 11)
    c.drawCentredString(W / 2, y, text.upper())


def body_center(c, lines, y, size=13, leading=22, color=MUTED):
    c.setFillColor(color)
    c.setFont("Helvetica", size)
    for line in lines:
        c.drawCentredString(W / 2, y, line)
        y -= leading
    return y


def gold_rule(c, y):
    c.setStrokeColor(GOLD)
    c.setLineWidth(1.5)
    c.line(W / 2 - 40, y, W / 2 + 40, y)


def s_cover(c):
    kicker(c, "VOLSHi", H - 170)
    c.setFillColor(WHITE)
    c.setFont("Helvetica-Bold", 44)
    c.drawCentredString(W / 2, H - 230, "The Span Between")
    c.setFillColor(GOLD)
    c.drawCentredString(W / 2, H - 285, "Intelligence and Human Experience")
    gold_rule(c, H - 320)
    body_center(c, ["Accountable intelligence — systems you can inspect,",
                    "memories you can trust, machines that show their work."], H - 360)
    # proof strip: THEIR numbers — what investors care about
    stats = [("$60B+", "TAM · trusted AI infra"), ("$20B", "SAM"),
             ("$100M", "SOM · ARR target"), ("€35M", "EU AI Act max fine")]
    x0 = W / 2 - 300
    y = 110
    for i, (num, label) in enumerate(stats):
        x = x0 + i * 200
        c.setFillColor(GOLD)
        c.setFont("Helvetica-Bold", 22)
        c.drawCentredString(x, y, num)
        c.setFillColor(MUTED)
        c.setFont("Helvetica", 9)
        c.drawCentredString(x, y - 18, label)


def s_problem(c):
    kicker(c, "The problem")
    title(c, "The black box era is over.")
    gold_rule(c, H - 200)
    body_center(c, [
        "AI models are interchangeable. They change under you.",
        "Every answer comes from a box nobody can open.",
        "No record of what was believed. No reason why. No accountability.",
        "",
        "You can't build civilization on a machine that can't show its work.",
    ], H - 250, size=14)


def s_thesis(c):
    kicker(c, "The thesis")
    c.setFillColor(WHITE)
    c.setFont("Helvetica-Bold", 30)
    c.drawCentredString(W / 2, H - 220, "\u201cI turn the black box")
    c.setFillColor(GOLD)
    c.drawCentredString(W / 2, H - 265, "into a plexiglass one.\u201d")
    gold_rule(c, H - 300)
    body_center(c, [
        "Every decision carries its record: what was believed,",
        "how strongly, when — and what came before.",
        "Inspectable by design. Not by promise.",
    ], H - 340, size=14)


def s_science(c):
    kicker(c, "The science")
    title(c, "A third clock for machine memory.")
    gold_rule(c, H - 200)
    body_center(c, [
        "Tick time. Event time. And knowledge time — when the system itself knew things.",
        "",
        "The Tritemporal Field Law: validated, published, timestamped.",
        "8/8 pre-registered predictions hit. 1,000+ researchers reading.",
        "DOI 10.5281/zenodo.23198458",
        "",
        "Memory as an attractor in a pressure landscape — not a row in a database.",
    ], H - 250, size=13)


def s_market(c):
    kicker(c, "The market")
    title(c, "The trusted layer beneath it all.")
    gold_rule(c, H - 200)
    tiers = [
        ("TAM", "$60B+", "Trusted AI infrastructure — governance, orchestration, memory."),
        ("SAM", "$20B", "The serviceable slice: VOLSHi's capabilities, VOLSHi's customers."),
        ("SOM", "$100M ARR", "The obtainable target — 0.5% of SAM."),
    ]
    y = H - 260
    for tier, num, desc in tiers:
        c.setFillColor(GOLD)
        c.setFont("Helvetica-Bold", 13)
        c.drawString(120, y, tier)
        c.setFillColor(WHITE)
        c.setFont("Helvetica-Bold", 22)
        c.drawString(190, y - 4, num)
        c.setFillColor(MUTED)
        c.setFont("Helvetica", 12)
        c.drawString(330, y, desc)
        y -= 52
    y -= 10
    c.setFillColor(GOLD)
    c.setFont("Helvetica", 10)
    c.drawCentredString(W / 2, y, "BOTTOM-UP · THREE PATHS TO $100M")
    y -= 28
    paths = ["100 customers × $1M ARR", "500 customers × $200K ARR", "1,000 customers × $100K ARR"]
    c.setFillColor(MUTED)
    c.setFont("Helvetica", 12)
    for p in paths:
        c.drawCentredString(W / 2, y, p)
        y -= 24


def s_field(c):
    kicker(c, "The mechanism")
    title(c, "The event field.")
    gold_rule(c, H - 200)
    body_center(c, [
        "Every event leaves pressure. Pressure shapes the landscape.",
        "The landscape pulls attention. Attention becomes behavior.",
        "",
        "Memory is not a row in a database —",
        "it is an attractor in the pressure landscape.",
        "The things attention cannot escape.",
    ], H - 250, size=14)


def s_engines(c):
    kicker(c, "Engines")
    title(c, "The family.")
    gold_rule(c, H - 200)
    items = [
        ("ARCHE", "The dad — attention engine. Allocates finite cognition to what matters now."),
        ("ERIE", "Triplet — epistemic retrieval. Evidence-backed knowledge with provenance."),
        ("ELLE", "Triplet — learning loop. Lessons survive the session that produced them."),
        ("KATIE", "Triplet — knowledge-authority indexing. The append-only record of belief."),
    ]
    y = H - 260
    for name, desc in items:
        c.setFillColor(GOLD)
        c.setFont("Helvetica-Bold", 15)
        c.drawString(120, y, name)
        c.setFillColor(MUTED)
        c.setFont("Helvetica", 13)
        c.drawString(230, y, desc)
        y -= 44


def s_builders_ops(c):
    kicker(c, "Builders · Operations")
    title(c, "Built to operate.")
    gold_rule(c, H - 200)
    items = [
        ("NIRMATA", "Persona engineering — specialized identities on the ARCHE engine."),
        ("ROSIE", "Autonomous software builder — intent to executable build."),
        ("BOUNCER", "Governance — authority and approval before consequential action."),
        ("PEEP + RATTER", "Observation — every execution sensed, every behavior telemetered."),
        ("CTRL TOWER", "Operator control — the whole machine, visible, in one surface."),
    ]
    y = H - 260
    for name, desc in items:
        c.setFillColor(GOLD)
        c.setFont("Helvetica-Bold", 14)
        c.drawString(110, y, name)
        c.setFillColor(MUTED)
        c.setFont("Helvetica", 12)
        c.drawString(280, y, desc)
        y -= 40


def s_apps_personas(c):
    kicker(c, "Applications · Personas")
    title(c, "Working systems, working identities.")
    gold_rule(c, H - 200)
    items = [
        ("SHERLOCK", "Evidence-first investigation — conclusions tied to their evidence."),
        ("WATSON", "Deterministic investigation engine + SDK."),
        ("SONDER", "Local-first workbench for VOLSHi intelligence."),
        ("Personas", "BRUNEL · CHIMERA · PSYRENE — persistent operating identities,"),
        ("", "with ArchePersona the first out of the forge."),
    ]
    y = H - 260
    for name, desc in items:
        if name:
            c.setFillColor(GOLD)
            c.setFont("Helvetica-Bold", 14)
            c.drawString(110, y, name)
        c.setFillColor(MUTED)
        c.setFont("Helvetica", 12)
        c.drawString(280, y, desc)
        y -= 40


def s_archetron(c):
    kicker(c, "The assembled machine")
    title(c, "ARCHETRON")
    c.setFillColor(GOLD)
    c.setFont("Helvetica", 13)
    c.drawCentredString(W / 2, H - 175, "SEVEN JOBS · ONE ARCHITECTURE")
    gold_rule(c, H - 200)
    body_center(c, [
        "Observe · Know · Attend · Learn · Govern · Act · Account",
        "",
        "Each job performed by one or more VOLSHi systems.",
        "Together, the larger machine. The parts become a system.",
    ], H - 250, size=14)


def s_ask(c):
    kicker(c, "VOLSHi")
    title(c, "Build the span with us.")
    gold_rule(c, H - 200)
    body_center(c, [
        "The model can change. The relationship shouldn't have to.",
        "",
        "Seeking: partners, pilots, and the team that builds what's next.",
        "",
        "founder@volshi.com",
    ], H - 250, size=14, color=WHITE)


SLIDES = [s_cover, s_problem, s_thesis, s_market, s_science, s_field,
          s_archetron, s_ask]

if __name__ == "__main__":
    slide(None)
