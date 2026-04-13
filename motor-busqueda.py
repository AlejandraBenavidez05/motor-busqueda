import numpy as np

# =========================
# DATASET - 10 artículos reales del Reglamento Académico Institucional
# Fundación Universitaria Konrad Lorenz (Acuerdo No. 01 - Enero 20 de 2025)
# =========================
documents = [
    "la institucion podra ofrecer programas academicos en niveles tecnico profesional tecnologico profesional universitario especializacion maestria y doctorado",  # Art. 1
    "la matricula es el acto mediante el cual la institucion reconoce formalmente a una persona como estudiante comprometida a cumplir estatutos y reglamentos",     # Art. 30
    "la matricula debe renovarse dentro de los plazos fijados en el calendario academico y expira finalizado el periodo academico cursado",                          # Art. 31
    "la matricula se cancela por decision voluntaria del estudiante o por las causales de perdida de la calidad de estudiante contempladas en el reglamento",        # Art. 32
    "la asistencia de los estudiantes es obligatoria en programas que dispongan de espacios formativos que impliquen presencialidad o mediacion tecnologica",        # Art. 42
    "el numero maximo de ausencias permitido en una asignatura es del veinte por ciento sobre el total de horas que la asignatura tiene en el periodo academico",    # Art. 43 Par. 1
    "cuando la inasistencia iguale o supere el porcentaje permitido la asignatura se califica con cero y el sistema la registra como reprobada por inasistencia",    # Art. 43 Par. 4
    "la condicion de estudiante se pierde por sanciones disciplinarias incumplimiento de obligaciones pecuniarias o perdida del cupo por motivos academicos",        # Art. 41
    "la evaluacion academica comprende actividades y procedimientos para valorar el alcance de los resultados de aprendizaje establecidos por el programa academico", # Art. 54
    "la calificacion aprobatoria minima para programas de pregrado es de treinta puntos y para especializaciones y maestrias es de treinta y cinco puntos"            # Art. 57
]

# =========================
# FUNCIONES TF - IDF
# =========================
def calcular_tf(palabra, doc):
    palabras = doc.split()
    return palabras.count(palabra) / len(palabras)

def calcular_idf(palabra, documentos):
    N = len(documentos)
    df = sum(1 for doc in documentos if palabra in doc)
    return np.log(N / (df + 1))  # +1 evita division por cero

def calcular_score(query, documentos):
    query_palabras = query.split()
    scores = []
    for i, doc in enumerate(documentos):
        score_total = 0
        for palabra in query_palabras:
            tf = calcular_tf(palabra, doc)
            idf = calcular_idf(palabra, documentos)
            score_total += tf * idf
        scores.append((i+1, score_total, doc))
    return sorted(scores, key=lambda x: x[1], reverse=True)

# =========================
# MOSTRAR RESULTADOS
# =========================
def buscar(query):
    print(f"\n🔎 Consulta: {query}\n")
    resultados = calcular_score(query, documents)
    for i, (doc_id, score, doc) in enumerate(resultados[:3], 1):
        print(f"{i}. Documento {doc_id}")
        print(f"   Texto: {doc}")
        print(f"   Score: {score:.4f}\n")

# =========================
# CALCULAR IDF GLOBAL
# =========================
def mostrar_idf():
    todas_palabras = set(" ".join(documents).split())
    idf_scores = [(p, calcular_idf(p, documents)) for p in todas_palabras]
    idf_scores.sort(key=lambda x: x[1])

    print("\n📉 5 palabras con IDF más bajo (más comunes en el corpus):")
    for p, v in idf_scores[:5]:
        print(f"  {p}: {v:.4f}")

    print("\n📈 5 palabras con IDF más alto (más únicas en el corpus):")
    for p, v in idf_scores[-5:]:
        print(f"  {p}: {v:.4f}")

# =========================
# PRUEBAS
# =========================
if __name__ == "__main__":
    mostrar_idf()
    buscar("matricula estudiante")
    buscar("inasistencia asignatura reprobada")
    buscar("evaluacion calificacion aprobatoria")
