# Código fuente de la charla "Documentation as code"
HacktoberFest Lima 2020 - Henry Tong
Video de la charla en AdaThinkLab  https://www.facebook.com/AdaThinkLab

## Introducción
Aquí encontrarás los ejemplos de código usados durante la charla. Este documento es además un ejemplo de uso de Markdown, si estás leyéndolo desde visual studio code puede tener una vista previa del resultado final haciendo CTRL+K V

## Instalación
- Utiliza Python 3.6+
- Se recomienda crear un ambiente de prueba (Python environment)
- Las librerías se pueden instalar con:
```
pip install -r requirements.txt
```

- Ejemplo de docker: Este proyecto necesita una base de datos postgresql, puede instalar una localmente con docker:
```
docker run -d --name sigep -e POSTGRES_PASSWORD=panasonic -p 5555:5432 postgres
```

## Otro ejemplo de readme
Puedes ver otro ejemplo de readme y uso de topics en github aquí https://github.com/maitelab/maitenotas/tree/v3
