FastAPI - Framework moderno para Criar API's Web com validação e tipagem, de forma rápida.

Utilidades:
- Criar API's Rest
- Aplicações Assíncronas
- Alta Performance e velocidade
- Desenvolvimento de Microserviços

Vantagens:
- Velocidade e Performance
- Simples de utilizar
- Documentação com Swagger
- Compatibilidade com async/await
- Tipagem Automática (valida dados e retorna erros sem precisar de validação manual.)

FastAPI x Django:
    Django: [
        - MVC com Admin, ORM e Autenticação
        - Robusto, porém mais lento
        - Tipagem e Validações Manuais via Serializers e Views
        - Ideal para Ecossistemas que necessitam de robustez e apps com paineis administrativos e front
        - Muitos recursos nativos
        - Mais complexo de aprender(Muitos recursos a se explorar, tipos de Views, Validações, Operações e etc)
    ]

    FastAPI: [
        - Focado em criar API's e consumo de API's, mas sem templates e ORM
        - Mais rápido e suporta async/await, porém com menos recursos nativos
        - Tipagem Automática no BaseModel(via Pydantic)
        - Ideal para API's modernas e Microserviços
        - Poucos recursos nativos e necessidade de personalização
        - Simples de Aprender
    ]
