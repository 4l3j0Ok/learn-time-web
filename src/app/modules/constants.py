from enum import Enum
import os


def get_content(technology: str, md_dir: str) -> str:
    return open(f"{os.getenv('APP_PATH')}/technologies/{md_dir}/{technology}.md").read()


class App(Enum):
    name = "Learn Time"
    author = "Alejo Sarmiento"
    version = "v1"
    url = os.getenv("APP_URL", "https://learn.alejoide.com")


class Default(Enum):
    icon_pack = "simple-icons"


class Languages(Enum):
    title = "Lenguajes"
    md_path = "langs"
    items = {
        "python": {
            "title": "Python",
            "content": get_content("python", md_path),
            "icon": f"{Default.icon_pack.value}:python",
            "page": "/python",
            "courses": [
                {
                    "title": "Ultimate Python",
                    "author": "Hola Mundo",
                    "image": "/images/courses/python/ultimate-python.webp",
                    "url": r"https://academia.holamundo.io/courses/ultimate-python",
                    "is_free": False,
                },
                {
                    "title": "Cursos de Python desde 0",
                    "author": "MoureDev",
                    "image": "/images/courses/python/python-mouredev.webp",
                    "url": r"https://www.youtube.com/playlist?list=PLNdFk2_brsRdgQXLIlKBXQDeRf3qvXVU_",
                    "is_free": True,
                },
                {
                    "title": "Qt/PySide: Interfaces Gráficas con Python",
                    "author": "Hektor Profe",
                    "image": "/images/courses/python/pyside.webp",
                    "url": r"https://cdn.hektorprofe.net/cupon/pyside",
                    "is_free": False,
                },
            ],
            "resources": [
                {
                    "title": "Web oficial",
                    "description": "Visita la web oficial de Python.",
                    "url": r"https://www.python.org/",
                    "image": "/images/resources/python-logo.webp",
                    "icon": f"{Default.icon_pack.value}:python",
                },
                {
                    "title": "Documentación oficial",
                    "description": "Visita la documentación oficial de Python.",
                    "url": r"https://docs.python.org/",
                    "image": "/images/resources/python-logo.webp",
                    "icon": f"{Default.icon_pack.value}:python",
                },
            ],
        },
        "javascript": {
            "title": "JavaScript",
            "content": get_content("javascript", md_path),
            "icon": "material-symbols:javascript",
            "page": "/javascript",
            "courses": [
                {
                    "title": "JavaScript desde CERO",
                    "author": "SoyDalto",
                    "image": "/images/courses/javascript/javascript-soy-dalto.webp",
                    "url": r"https://www.youtube.com/playlist?list=PLE8uP447fYpiBqMVF1hdWl9uFeVEeXRTm",
                    "is_free": True,
                },
                {
                    "title": "Introducción a JavaScript",
                    "author": "Midudev",
                    "image": "/images/courses/javascript/intro-javascript-midudev.webp",
                    "url": r"https://youtu.be/Z34BF9PCfYg?si=2iZILAq9q28ADmM0",
                    "is_free": True,
                },
                {
                    "title": "Ultimate JavaScript",
                    "author": "Hola Mundo",
                    "image": "/images/courses/javascript/ultimate-javascript.webp",
                    "url": r"https://academia.holamundo.io/courses/ultimate-javascript",
                    "is_free": False,
                },
                {
                    "title": "Ultimate React",
                    "author": "Hola Mundo",
                    "image": "/images/courses/javascript/ultimate-react.webp",
                    "url": r"https://academia.holamundo.io/courses/ultimate-react",
                    "is_free": False,
                },
                {
                    "title": "Bootcamp FullStack Gratuito",
                    "author": "Midudev",
                    "image": "/images/courses/javascript/bootcamp-fullstack-midudev.webp",
                    "url": r"https://www.youtube.com/playlist?list=PLV8x_i1fqBw0Kn_fBIZTa3wS_VZAqddX7",
                    "is_free": True,
                },
                {
                    "title": "Curso de Node.js completo",
                    "author": "Midudev",
                    "image": "/images/courses/javascript/nodejs-midudev.webp",
                    "url": r"https://www.youtube.com/playlist?list=PLUofhDIg_38qm2oPOV-IRTTEKyrVBBaU7",
                    "is_free": True,
                },
                {
                    "title": "Aprende Angular 17 desde 0",
                    "author": "Midudev",
                    "image": "/images/courses/javascript/angular-midudev.webp",
                    "url": r"https://youtu.be/f7unUpshmpA?si=IIrqTn8ZB5u_hN_m",
                    "is_free": True,
                },
            ],
        },
        "csharp": {
            "title": "C#",
            "content": get_content("csharp", md_path),
            "icon": f"{Default.icon_pack.value}:csharp",
            "page": "/csharp",
        },
        "java": {
            "title": "Java",
            "content": get_content("java", md_path),
            "icon": "ri:java-line",
            "page": "/java",
        },
        "html": {
            "title": "HTML",
            "content": get_content("html", md_path),
            "icon": "akar-icons:html-fill",
            "page": "/html",
        },
        "cplusplus": {
            "title": "C++",
            "content": get_content("cplusplus", md_path),
            "icon": f"{Default.icon_pack.value}:cplusplus",
            "page": "/cplusplus",
        },
        "typescript": {
            "title": "TypeScript",
            "content": get_content("typescript", md_path),
            "icon": f"{Default.icon_pack.value}:typescript",
            "page": "/typescript",
        },
        "go": {
            "title": "Go",
            "content": get_content("go", md_path),
            "icon": f"{Default.icon_pack.value}:go",
            "page": "/go",
        },
        "c": {
            "title": "C",
            "content": get_content("c", md_path),
            "icon": f"{Default.icon_pack.value}:c",
            "page": "/c",
        },
        "rust": {
            "title": "Rust",
            "content": get_content("rust", md_path),
            "icon": f"{Default.icon_pack.value}:rust",
            "page": "/rust",
        },
        "ruby": {
            "title": "Ruby",
            "content": get_content("ruby", md_path),
            "icon": f"{Default.icon_pack.value}:ruby",
            "page": "/ruby",
        },
        "php": {
            "title": "PHP",
            "content": get_content("php", md_path),
            "icon": "devicon-plain:php",
            "page": "/php",
        },
        "dart": {
            "title": "Dart",
            "content": get_content("dart", md_path),
            "icon": f"{Default.icon_pack.value}:dart",
            "page": "/dart",
        },
        "kotlin": {
            "title": "Kotlin",
            "content": get_content("kotlin", md_path),
            "icon": "cib:kotlin",
            "page": "/kotlin",
        },
        "swift": {
            "title": "Swift",
            "content": get_content("swift", md_path),
            "icon": f"{Default.icon_pack.value}:swift",
            "page": "/swift",
        },
    }


class DevOps(Enum):
    title = "Infraestructura y DevOps"
    md_dir = "devops"
    items = {
        "git": {
            "title": "Git",
            "content": get_content("git", md_dir),
            "icon": f"{Default.icon_pack.value}:git",
            "page": "/git",
        },
        "docker": {
            "title": "Docker",
            "content": get_content("docker", md_dir),
            "icon": f"{Default.icon_pack.value}:docker",
            "page": "/docker",
        },
        "kubernetes": {
            "title": "Kubernetes",
            "content": get_content("kubernetes", md_dir),
            "icon": f"{Default.icon_pack.value}:kubernetes",
            "page": "/kubernetes",
        },
        "ci-cd": {
            "title": "CI/CD",
            "content": get_content("ci-cd", md_dir),
            "icon": "clarity:ci-cd-line",
            "page": "/ci-cd",
        },
        "bash": {
            "title": "Bash",
            "content": get_content("bash", md_dir),
            "icon": "devicon-plain:bash",
            "page": "/bash",
        },
        "powershell": {
            "title": "PowerShell",
            "content": get_content("powershell", md_dir),
            "icon": f"{Default.icon_pack.value}:powershell",
            "page": "/powershell",
        },
    }
