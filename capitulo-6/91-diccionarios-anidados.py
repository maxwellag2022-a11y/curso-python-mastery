academia = {
    "nombre":"Academia Fibonacci",
    "Pais":"Guatemala",
    "Cursos": {
        "Python": {
            "duracion_meses" : 10,
            "precio": 1500,
            "instructor" : "Luis"
        },
        "javascript" : {
            "duracion_meses" : 12,
            "precio": 1200,
            "instructor" : "Maria"
        },
    },
    "fundado": 2024
}

print(academia["Cursos"]["Python"]["instructor"])
print(academia["Cursos"]["javascript"]["precio"])

academia["Cursos"]["Python"]["precio"] = 1000

print(academia)