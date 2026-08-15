"""Gera os PDFs do currículo (PT e EN) a partir dos mesmos dados usados no site (src/data.js)."""

import os
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib.colors import HexColor
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    ListFlowable,
    ListItem,
    HRFlowable,
)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PUBLIC_DIR = os.path.join(BASE_DIR, "public")

ACCENT = HexColor("#2f6fdb")
TEXT = HexColor("#1c2230")
MUTED = HexColor("#5a6272")
BORDER = HexColor("#d8dce4")

CONTENT = {
    "pt": {
        "output_file": "Nedymar-Schuabe-Curriculo.pdf",
        "section_titles": {
            "about": "Sobre",
            "experience": "Experiência",
            "education": "Formação acadêmica",
            "certifications": "Certificações",
        },
        "profile": {
            "name": "Nedymar Schuabe",
            "title": "Analista e Desenvolvedor de Sistemas",
            "subtitle": "Oracle PL/SQL · DBA Júnior · Node.js · Python · React",
            "phone": "54 99684-2203",
            "email": "nedymar.schuabe@outlook.com",
            "linkedin": "linkedin.com/in/nedymarschuabe",
            "github": "github.com/nedymarschuabe",
            "summary": (
                "Analista e Desenvolvedor de Sistemas com mais de 5 anos de experiência, atualmente "
                "responsável pela sustentação N2 do sistema MV na Clínica Kozma, atuando com Oracle, "
                "PL/SQL, análise de requisitos, correção de incidentes e otimização de consultas. Já "
                "atuei no desenvolvimento de integrações críticas utilizadas por hospitais da rede DASA, "
                "com alta estabilidade e redução de falhas. Também construo soluções com Oracle Database, "
                "SQL, PL/SQL, Node.js, Python e React, participando de integrações, automações de "
                "processos e melhorias de performance em aplicações corporativas."
            ),
        },
        "core_skills": [
            "Oracle Database", "SQL e PL/SQL", "Sistema MV", "Sustentação N2",
            "Integração de Sistemas", "APIs REST", "Node.js", "Python", "React",
            "Performance e Otimização SQL", "Análise de Sistemas", "AWS Lambda",
            "HL7 FHIR / HL7 v2", "PostgreSQL", "Git",
        ],
        "experiences": [
            {
                "role": "Analista e Desenvolvedor de Sistema MV N2",
                "company": "Clínica Kozma",
                "period": "outubro de 2024 - Presente (1 ano 11 meses)",
                "location": "Passo Fundo, Rio Grande do Sul, Brasil",
                "description": (
                    "Responsável pela sustentação, análise e desenvolvimento de soluções voltadas ao ambiente "
                    "hospitalar utilizando o sistema MV e banco de dados Oracle."
                ),
                "bullets": [
                    "Desenvolvimento e manutenção de rotinas PL/SQL.",
                    "Análise e correção de incidentes de sustentação N2.",
                    "Desenvolvimento de consultas SQL para suporte às áreas de negócio.",
                    "Integração entre sistemas utilizando APIs e serviços.",
                    "Otimização de performance em consultas e processos de banco de dados.",
                    "Desenvolvimento de automações utilizando Node.js e Python.",
                    "Desenvolvimento de dashboards utilizando API em TypeScript e React.",
                ],
            },
            {
                "role": "Analista de sistemas",
                "company": "Agrodanieli Ind. Com. Ltda",
                "period": "janeiro de 2024 - outubro de 2024 (10 meses)",
                "location": "Tapejara, Rio Grande do Sul, Brasil",
                "description": (
                    "Análise de regras de negócio, investigação técnica de objetos de banco (PL/SQL, T-SQL e "
                    "PL/pgSQL) e automação de processos corporativos."
                ),
                "bullets": [
                    "Análise de processos e fluxo de dados, identificando gargalos e propondo melhorias.",
                    "Investigação técnica de objetos de banco (procedures, functions, views e consultas).",
                    "Ajustes e validações de regras de negócio aplicadas aos sistemas corporativos.",
                    "Diagnóstico e automação de processos para agilizar atividades do usuário.",
                    "Suporte técnico direto a equipes internas e fornecedores.",
                ],
            },
            {
                "role": "Analista e Desenvolvedor de Integrações",
                "company": "DataIntegra",
                "period": "março de 2021 - janeiro de 2024 (2 anos 11 meses)",
                "location": "Passo Fundo, RS",
                "description": (
                    "Atuei como desenvolvedor responsável por integrações críticas em ambiente hospitalar, "
                    "com foco em Oracle PL/SQL, performance e qualidade de dados."
                ),
                "bullets": [
                    "Desenvolvimento avançado em Oracle PL/SQL: procedures, functions, packages, triggers, views e jobs.",
                    "Otimização de consultas críticas com análise de plano de execução e tuning.",
                    "Construção de integrações hospitalares (cadastro, agendamento e movimentação de pacientes).",
                    "Desenvolvimento de APIs serverless em AWS Lambda (Python).",
                    "Atuação com padrões HL7 FHIR e HL7 v2 em interoperabilidade hospitalar.",
                    "Manutenção de serviços XML/XSLT em ambiente Tomcat.",
                    "Vivência prática nos módulos MV (MV2000 e SOULMV HTML5).",
                    "Entrega de integrações críticas utilizadas por hospitais da DASA, com alta estabilidade.",
                ],
            },
            {
                "role": "Analista de sistema",
                "company": "Agrodanieli Ind. Com. Ltda",
                "period": "agosto de 2016 - março de 2021 (4 anos 8 meses)",
                "location": "Tapejara, Rio Grande do Sul, Brasil",
                "description": (
                    "Suporte técnico, levantamento de requisitos e melhorias de processos, incluindo a Fábrica "
                    "de Ração (ambiente 100% automatizado)."
                ),
                "bullets": [
                    "Atendimento a usuários internos, análise de problemas e implementação de soluções.",
                    "Mediação entre empresa e fornecedores terceirizados.",
                    "Manipulação de dados e criação de consultas SQL em Oracle.",
                    "Mapeamento e melhoria de processos em áreas críticas.",
                    "Gestão de chamados via Qualitor e acompanhamento ponta a ponta das demandas.",
                ],
            },
        ],
        "education": [
            ("Cruzeiro do Sul Virtual", "Análise e Desenvolvimento de Sistemas, Information Technology", "fevereiro de 2021 - dezembro de 2023"),
            ("Unyleya", "Inteligência Artificial em Serviços de Saúde, Information Technology", "agosto de 2025 - março de 2026"),
        ],
        "certifications": [
            "Análise e Desenvolvimento de Sistemas",
            "Boas práticas de SQL Banco de Dados Relacional",
            "Introdução ao Ruby",
            "SQL Server: Formação Básica",
            "Inglês - A1",
        ],
    },
    "en": {
        "output_file": "Nedymar-Schuabe-Resume-EN.pdf",
        "section_titles": {
            "about": "About",
            "experience": "Experience",
            "education": "Academic Education",
            "certifications": "Certifications",
        },
        "profile": {
            "name": "Nedymar Schuabe",
            "title": "Systems Analyst and Developer",
            "subtitle": "Oracle PL/SQL · Junior DBA · Node.js · Python · React",
            "phone": "54 99684-2203",
            "email": "nedymar.schuabe@outlook.com",
            "linkedin": "linkedin.com/in/nedymarschuabe",
            "github": "github.com/nedymarschuabe",
            "summary": (
                "Systems Analyst and Developer with 5+ years of experience, currently responsible for "
                "N2 support of the MV system at Clínica Kozma, working with Oracle, PL/SQL, requirements "
                "analysis, incident resolution, and query optimization. I have previously developed "
                "critical integrations used by DASA network hospitals, with high stability and reduced "
                "failures. I also build solutions with Oracle Database, SQL, PL/SQL, Node.js, Python, "
                "and React, contributing to integrations, process automation, and performance "
                "improvements in corporate applications."
            ),
        },
        "core_skills": [
            "Oracle Database", "SQL & PL/SQL", "MV System", "N2 Support",
            "Systems Integration", "REST APIs", "Node.js", "Python", "React",
            "SQL Performance & Optimization", "Systems Analysis", "AWS Lambda",
            "HL7 FHIR / HL7 v2", "PostgreSQL", "Git",
        ],
        "experiences": [
            {
                "role": "Systems Analyst and Developer - MV N2 Support",
                "company": "Clínica Kozma",
                "period": "October 2024 - Present (1 year 11 months)",
                "location": "Passo Fundo, Rio Grande do Sul, Brazil",
                "description": (
                    "Responsible for support, analysis, and development of solutions for the hospital "
                    "environment using the MV system and Oracle database."
                ),
                "bullets": [
                    "Development and maintenance of PL/SQL routines.",
                    "Analysis and resolution of N2 support incidents.",
                    "Development of SQL queries to support business areas.",
                    "System integration using APIs and services.",
                    "Performance optimization of database queries and processes.",
                    "Development of automations using Node.js and Python.",
                    "Development of dashboards using TypeScript and React APIs.",
                ],
            },
            {
                "role": "Systems Analyst",
                "company": "Agrodanieli Ind. Com. Ltda",
                "period": "January 2024 - October 2024 (10 months)",
                "location": "Tapejara, Rio Grande do Sul, Brazil",
                "description": (
                    "Analysis of business rules, technical investigation of database objects (PL/SQL, "
                    "T-SQL, and PL/pgSQL), and automation of corporate processes."
                ),
                "bullets": [
                    "Process and data flow analysis, identifying bottlenecks and proposing improvements.",
                    "Technical investigation of database objects (procedures, functions, views, and queries).",
                    "Adjustments and validation of business rules applied to corporate systems.",
                    "Diagnosis and automation of processes to speed up user activities.",
                    "Direct technical support to internal teams and vendors.",
                ],
            },
            {
                "role": "Integrations Analyst and Developer",
                "company": "DataIntegra",
                "period": "March 2021 - January 2024 (2 years 11 months)",
                "location": "Passo Fundo, RS",
                "description": (
                    "Worked as the developer responsible for critical integrations in the hospital "
                    "environment, focused on Oracle PL/SQL, performance, and data quality."
                ),
                "bullets": [
                    "Advanced development in Oracle PL/SQL: procedures, functions, packages, triggers, views, and jobs.",
                    "Optimization of critical queries through execution plan analysis and tuning.",
                    "Built hospital integrations (patient registration, scheduling, and movement).",
                    "Development of serverless APIs on AWS Lambda (Python).",
                    "Worked with HL7 FHIR and HL7 v2 standards for hospital interoperability.",
                    "Maintenance of XML/XSLT services on Tomcat.",
                    "Hands-on experience with MV modules (MV2000 and SOULMV HTML5).",
                    "Delivered critical integrations used by DASA network hospitals, with high stability.",
                ],
            },
            {
                "role": "Systems Analyst",
                "company": "Agrodanieli Ind. Com. Ltda",
                "period": "August 2016 - March 2021 (4 years 8 months)",
                "location": "Tapejara, Rio Grande do Sul, Brazil",
                "description": (
                    "Technical support, requirements gathering, and process improvements, including the "
                    "Feed Mill (a fully automated environment)."
                ),
                "bullets": [
                    "Support for internal users, problem analysis, and solution implementation.",
                    "Mediation between the company and third-party vendors.",
                    "Data manipulation and SQL query creation in Oracle.",
                    "Mapping and improvement of processes in critical areas.",
                    "Ticket management via Qualitor and end-to-end demand tracking.",
                ],
            },
        ],
        "education": [
            ("Cruzeiro do Sul Virtual", "Systems Analysis and Development, Information Technology", "February 2021 - December 2023"),
            ("Unyleya", "Artificial Intelligence in Healthcare Services, Information Technology", "August 2025 - March 2026"),
        ],
        "certifications": [
            "Systems Analysis and Development",
            "SQL Best Practices - Relational Database",
            "Introduction to Ruby",
            "SQL Server: Basic Training",
            "English - A1",
        ],
    },
}


def build_styles():
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(
        name="NameStyle", fontName="Helvetica-Bold", fontSize=22, leading=26, textColor=TEXT,
        spaceAfter=2,
    ))
    styles.add(ParagraphStyle(
        name="TitleStyle", fontName="Helvetica", fontSize=12, leading=15, textColor=ACCENT,
        spaceAfter=2,
    ))
    styles.add(ParagraphStyle(
        name="SubtitleStyle", fontName="Helvetica", fontSize=9.5, leading=12, textColor=MUTED,
        spaceAfter=2,
    ))
    styles.add(ParagraphStyle(
        name="ContactStyle", fontName="Helvetica", fontSize=9, leading=12, textColor=MUTED,
        spaceAfter=10,
    ))
    styles.add(ParagraphStyle(
        name="SectionHeading", fontName="Helvetica-Bold", fontSize=13, leading=16, textColor=TEXT,
        spaceBefore=14, spaceAfter=6,
    ))
    styles.add(ParagraphStyle(
        name="BodyText2", fontName="Helvetica", fontSize=9.5, textColor=TEXT,
        leading=14, spaceAfter=6,
    ))
    styles.add(ParagraphStyle(
        name="RoleStyle", fontName="Helvetica-Bold", fontSize=10.5, leading=13, textColor=TEXT,
        spaceAfter=1,
    ))
    styles.add(ParagraphStyle(
        name="MetaStyle", fontName="Helvetica-Oblique", fontSize=9, leading=12, textColor=MUTED,
        spaceAfter=4,
    ))
    styles.add(ParagraphStyle(
        name="BulletText", fontName="Helvetica", fontSize=9.2, textColor=TEXT,
        leading=13,
    ))
    styles.add(ParagraphStyle(
        name="SkillChip", fontName="Helvetica", fontSize=8.7, leading=13, textColor=ACCENT,
    ))
    return styles


def make_bullets(items, styles):
    return ListFlowable(
        [ListItem(Paragraph(item, styles["BulletText"]), spaceAfter=2) for item in items],
        bulletType="bullet",
        start="•",
        bulletFontSize=8,
        leftIndent=12,
    )


def build_pdf(lang_data):
    styles = build_styles()
    profile = lang_data["profile"]
    titles = lang_data["section_titles"]
    output_path = os.path.join(PUBLIC_DIR, lang_data["output_file"])

    doc = SimpleDocTemplate(
        output_path,
        pagesize=A4,
        topMargin=18 * mm,
        bottomMargin=16 * mm,
        leftMargin=18 * mm,
        rightMargin=18 * mm,
        title=f"{profile['name']} - {profile['title']}",
        author=profile["name"],
    )

    story = []

    story.append(Paragraph(profile["name"], styles["NameStyle"]))
    story.append(Paragraph(profile["title"], styles["TitleStyle"]))
    story.append(Paragraph(profile["subtitle"], styles["SubtitleStyle"]))
    contact_line = (
        f"{profile['email']} &nbsp;·&nbsp; {profile['phone']} &nbsp;·&nbsp; "
        f"{profile['linkedin']} &nbsp;·&nbsp; {profile['github']}"
    )
    story.append(Paragraph(contact_line, styles["ContactStyle"]))
    story.append(HRFlowable(width="100%", thickness=0.8, color=BORDER, spaceAfter=8))

    story.append(Paragraph(titles["about"], styles["SectionHeading"]))
    story.append(Paragraph(profile["summary"], styles["BodyText2"]))

    skills_text = " &nbsp;•&nbsp; ".join(lang_data["core_skills"])
    story.append(Paragraph(skills_text, styles["SkillChip"]))

    story.append(Paragraph(titles["experience"], styles["SectionHeading"]))
    for job in lang_data["experiences"]:
        story.append(Paragraph(job["role"], styles["RoleStyle"]))
        story.append(Paragraph(
            f"{job['company']} · {job['period']} · {job['location']}", styles["MetaStyle"]
        ))
        story.append(Paragraph(job["description"], styles["BodyText2"]))
        story.append(make_bullets(job["bullets"], styles))
        story.append(Spacer(1, 8))

    story.append(Paragraph(titles["education"], styles["SectionHeading"]))
    for school, degree, period in lang_data["education"]:
        story.append(Paragraph(school, styles["RoleStyle"]))
        story.append(Paragraph(degree, styles["BodyText2"]))
        story.append(Paragraph(period, styles["MetaStyle"]))

    story.append(Paragraph(titles["certifications"], styles["SectionHeading"]))
    story.append(make_bullets(lang_data["certifications"], styles))

    doc.build(story)
    print(f"PDF gerado em: {output_path}")


if __name__ == "__main__":
    os.makedirs(PUBLIC_DIR, exist_ok=True)
    for lang_data in CONTENT.values():
        build_pdf(lang_data)
