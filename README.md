# API para Administração de salas.

## Endpoints
### GET /login
Esse endpoint é responsável pelo o login do usuário.
#### Paramêtros
Nenhum
#### Respostas
##### OK! 200
Caso essa resposta aconteça você vai receber um token. Exemplos de resposta:

```
##### Falha na autenticação! 401
Caso essa resposta aconteça, isso significa que aconteceu alguma falha durante o processo. Motivos: Tokne inválido, Token expirado.

Exemplo de resposta: 
```
{
    "err": "Token Inválido!"
}

```

## Endpoints
### POST /login
Esse endpoint é responsável por retornar o processo de Login de Usúarios.
#### Paramêtros
email: Usuário do usuário cadastrado no sistema.
password: Senha do usuário cadastrado no sistema com aquele determiando Usúario.

Exemplo:
```
{
    "login": "Mateus Alves",
    "password": "1234"
}
```
#### Respostas
##### OK! 200
Caso essa resposta aconteça você vai receber o token JWT para conseguir acessar endpoints protegidos na API. 

Exemplos de resposta:
```
{
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.ey"
}

```
##### Falha na autenticação! 401
Caso essa resposta aconteça, isso significa que aconteceu alguma falha durante o processo. Motivos: senha ou login incorretos.

Exemplo de resposta: 
```
 {err: "Crendenciais inválidas"}
```

