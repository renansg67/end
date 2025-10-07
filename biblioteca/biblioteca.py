import streamlit as st

col1, col2, col3 = st.columns([1, 3, 1])

biblioteca = [
    {
        "id": "L001",
        "titulo": "Ultrasonic Testing of Materials",
        "autor": "J. Krautkrämer, H. Krautkrämer",
        "ano": 1990,
        "categoria": "Ultrassom",
        "subcategoria": "Tomografia acústica",
        "idioma": "Inglês",
        "editora": "Springer-Verlag",
        "isbn": "978-3-540-10245-6",
        "palavras_chave": ["ultrassom", "detecção", "falhas", "END"],
        "tipo_de_material": "Livro",
        "nivel": "Pós-graduação",
        "localizacao_fisica": "Estante 2 – Prateleira C",
        "disponibilidade": "Disponível",
        "resumo": "Referência clássica sobre princípios de ensaios ultrassônicos em materiais metálicos e não metálicos.",
        "imagem_capa_url": "https://upload.wikimedia.org/wikipedia/commons/.../exemplo.jpg",
        "link_externo": "https://books.google.com/...",
        "data_de_entrada": "2025-10-07"
    },
    {
        "id": "L002",
        "titulo": "Ensaios Não Destrutivos – Princípios e Aplicações",
        "autor": "Charles Hellier",
        "ano": 2012,
        "categoria": "Ultrassom",
        "subcategoria": "Aplicações industriais",
        "idioma": "Português",
        "editora": "McGraw-Hill",
        "isbn": "978-0-07-177714-8",
        "palavras_chave": ["END", "ultrassom", "soldas", "inspeção"],
        "tipo_de_material": "Livro",
        "nivel": "Graduação",
        "localizacao_fisica": "Estante 1 – Prateleira A",
        "disponibilidade": "Emprestado",
        "resumo": "Aborda conceitos fundamentais dos ensaios não destrutivos e suas principais técnicas.",
        "imagem_capa_url": "https://upload.wikimedia.org/wikipedia/commons/.../hellier.jpg",
        "link_externo": "https://books.google.com/...",
        "data_de_entrada": "2025-10-07"
    },
    {
        "id": "",  # Identificador único do livro (ex: L001)
        "titulo": "Manual de Projeto e Construção de Pontes de Madeira",  # Título completo do livro
        "autor": "",  # Nome(s) do(s) autor(es)
        "ano": None,  # Ano de publicação (ex: 2025)
        "categoria": "",  # Tema principal (ex: Ultrassom)
        "subcategoria": "",  # Tema mais específico (ex: Tomografia acústica)
        "idioma": "",  # Idioma do livro (ex: Português, Inglês)
        "editora": "SET - EESC, USP",  # Nome da editora
        "isbn": "",  # Código ISBN, se houver
        "palavras_chave": [],  # Lista de palavras-chave (ex: ["ultrassom", "falhas"])
        "tipo_de_material": "Artigo",  # Livro, apostila, manual, tese, artigo
        "nivel": "Graduação",  # Público-alvo (Graduação, Pós, Técnico)
        "localizacao_fisica": "",  # Onde está o exemplar (ex: Estante 2 – Prateleira C)
        "disponibilidade": "",  # Disponível, Emprestado, Reservado
        "resumo": "",  # Breve descrição do conteúdo
        "imagem_capa_url": "",  # Link para imagem da capa (Drive, Wikimedia, etc.)
        "link_externo": "",  # Link para referência externa (ISBN, Google Books)
        "data_de_entrada": "2025-10-07"  # Data que o livro foi catalogado (YYYY-MM-DD)
    },
    {
        "id": "",  # Identificador único do livro (ex: L001)
        "titulo": "Compuestos Biomassa Vegetal y Cemento",  # Título completo do livro
        "autor": "Antonio L. Beraldo",  # Nome(s) do(s) autor(es)
        "ano": "2005",  # Ano de publicação (ex: 2025)
        "categoria": "",  # Tema principal (ex: Ultrassom)
        "subcategoria": "",  # Tema mais específico (ex: Tomografia acústica)
        "idioma": "Espanhol",  # Idioma do livro (ex: Português, Inglês)
        "editora": "",  # Nome da editora
        "isbn": "",  # Código ISBN, se houver
        "palavras_chave": [],  # Lista de palavras-chave (ex: ["ultrassom", "falhas"])
        "tipo_de_material": "Artigo",  # Livro, apostila, manual, tese, artigo
        "nivel": "Graduação",  # Público-alvo (Graduação, Pós, Técnico)
        "localizacao_fisica": "",  # Onde está o exemplar (ex: Estante 2 – Prateleira C)
        "disponibilidade": "",  # Disponível, Emprestado, Reservado
        "resumo": "",  # Breve descrição do conteúdo
        "imagem_capa_url": "",  # Link para imagem da capa (Drive, Wikimedia, etc.)
        "link_externo": "",  # Link para referência externa (ISBN, Google Books)
        "data_de_entrada": "2025-10-07"  # Data que o livro foi catalogado (YYYY-MM-DD)
    },
    {
        "id": "",  # Identificador único do livro (ex: L001)
        "titulo": "Rigidez da madeira obtida a partir da avaliação acústica na árvore",  # Título completo do livro
        "autor": "Cinthya Bertoldo Pedroso",  # Nome(s) do(s) autor(es)
        "ano": 2014,  # Ano de publicação (ex: 2025)
        "categoria": "",  # Tema principal (ex: Ultrassom)
        "subcategoria": "",  # Tema mais específico (ex: Tomografia acústica)
        "idioma": "",  # Idioma do livro (ex: Português, Inglês)
        "editora": "",  # Nome da editora
        "isbn": "",  # Código ISBN, se houver
        "palavras_chave": [
            "Propagação de ondas",
            "Velocidade na tora",
            "Velocidade na viga",
            "Diâmetro a altura do peito"
            "Densidade saturada",
            "Coeficiente de Poisson"
        ],  # Lista de palavras-chave (ex: ["ultrassom", "falhas"])
        "tipo_de_material": "Tese",  # Livro, apostila, manual, tese, artigo
        "nivel": "",  # Público-alvo (Graduação, Pós, Técnico)
        "localizacao_fisica": "",  # Onde está o exemplar (ex: Estante 2 – Prateleira C)
        "disponibilidade": "",  # Disponível, Emprestado, Reservado
        "resumo": "",  # Breve descrição do conteúdo
        "imagem_capa_url": "",  # Link para imagem da capa (Drive, Wikimedia, etc.)
        "link_externo": "",  # Link para referência externa (ISBN, Google Books)
        "data_de_entrada": "2025-10-07"  # Data que o livro foi catalogado (YYYY-MM-DD)
    },
    {
        "id": "",  # Identificador único do livro (ex: L001)
        "titulo": "Fundamentos de las propiedades físicas y mecánicas de las maderas",  # Título completo do livro
        "autor": "Eduardo O. Coronel",  # Nome(s) do(s) autor(es)
        "ano": 1994,  # Ano de publicação (ex: 2025)
        "categoria": "",  # Tema principal (ex: Ultrassom)
        "subcategoria": "",  # Tema mais específico (ex: Tomografia acústica)
        "idioma": "Espanhol",  # Idioma do livro (ex: Português, Inglês)
        "editora": "Editorial El Liberal",  # Nome da editora
        "isbn": "9504360610",  # Código ISBN, se houver
        "palavras_chave": [],  # Lista de palavras-chave (ex: ["ultrassom", "falhas"])
        "tipo_de_material": "Livro",  # Livro, apostila, manual, tese, artigo
        "nivel": "Pós",  # Público-alvo (Graduação, Pós, Técnico)
        "localizacao_fisica": "",  # Onde está o exemplar (ex: Estante 2 – Prateleira C)
        "disponibilidade": "",  # Disponível, Emprestado, Reservado
        "resumo": "",  # Breve descrição do conteúdo
        "imagem_capa_url": "",  # Link para imagem da capa (Drive, Wikimedia, etc.)
        "link_externo": "",  # Link para referência externa (ISBN, Google Books)
        "data_de_entrada": "2025-10-07"  # Data que o livro foi catalogado (YYYY-MM-DD)
    },
    {
        "id": "",  # Identificador único do livro (ex: L001)
        "titulo": "LA GESTIÓN Y EL APROVECHAMIENTO DE LOS RESIDUOS EN LA INDUSTRIA DE LA MADERA",  # Título completo do livro
        "autor": "Gregorio Antolín",  # Nome(s) do(s) autor(es)
        "ano": 2006,  # Ano de publicação (ex: 2025)
        "categoria": "",  # Tema principal (ex: Ultrassom)
        "subcategoria": "",  # Tema mais específico (ex: Tomografia acústica)
        "idioma": "Espanhol",  # Idioma do livro (ex: Português, Inglês)
        "editora": "Instituto Nacional de Tecnologia Industrial Madera y Muebles",  # Nome da editora
        "isbn": "",  # Código ISBN, se houver
        "palavras_chave": [],  # Lista de palavras-chave (ex: ["ultrassom", "falhas"])
        "tipo_de_material": "Livro",  # Livro, apostila, manual, tese, artigo
        "nivel": "Pós",  # Público-alvo (Graduação, Pós, Técnico)
        "localizacao_fisica": "",  # Onde está o exemplar (ex: Estante 2 – Prateleira C)
        "disponibilidade": "",  # Disponível, Emprestado, Reservado
        "resumo": "",  # Breve descrição do conteúdo
        "imagem_capa_url": "",  # Link para imagem da capa (Drive, Wikimedia, etc.)
        "link_externo": "",  # Link para referência externa (ISBN, Google Books)
        "data_de_entrada": "2025-10-07"  # Data que o livro foi catalogado (YYYY-MM-DD)
    },
    {
        "id": "",  # Identificador único do livro (ex: L001)
        "titulo": "Tecnologia para pré-dimensionamento de estrutura metálica",  # Título completo do livro
        "autor": "",  # Nome(s) do(s) autor(es)
        "ano": 1998,  # Ano de publicação (ex: 2025)
        "categoria": "",  # Tema principal (ex: Ultrassom)
        "subcategoria": "",  # Tema mais específico (ex: Tomografia acústica)
        "idioma": "Português",  # Idioma do livro (ex: Português, Inglês)
        "editora": "AltoQI Tecnologia em Informação Ltda.",  # Nome da editora
        "isbn": "",  # Código ISBN, se houver
        "palavras_chave": [],  # Lista de palavras-chave (ex: ["ultrassom", "falhas"])
        "tipo_de_material": "",  # Livro, apostila, manual, tese, artigo
        "nivel": "Graduação",  # Público-alvo (Graduação, Pós, Técnico)
        "localizacao_fisica": "",  # Onde está o exemplar (ex: Estante 2 – Prateleira C)
        "disponibilidade": "",  # Disponível, Emprestado, Reservado
        "resumo": "",  # Breve descrição do conteúdo
        "imagem_capa_url": "",  # Link para imagem da capa (Drive, Wikimedia, etc.)
        "link_externo": "",  # Link para referência externa (ISBN, Google Books)
        "data_de_entrada": "2025-10-07"  # Data que o livro foi catalogado (YYYY-MM-DD)
    }
]

st.write(biblioteca)

col2.info("Biblioteca")