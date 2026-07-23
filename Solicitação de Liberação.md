Assunto: Solicitação de Liberação de Acesso ao SQL Server via VS Code – Treinamento/Capacitação

Olá, equipe de Suporte/TI,

Espero que estejam bem.

Gostaria de solicitar a liberação e liberação de permissões nos computadores dos participantes para a realização do treinamento de SQL Server utilizando o Visual Studio Code.

Para garantir que todos consigam realizar os exercícios práticos sem bloqueios de rede, firewall ou restrições de sistema, solicitamos os seguintes acessos/liberações:

Permissões na Instalação / Instância Local:

Permissão no serviço local do SQL Server (MSSQLSERVER ou SQLEXPRESS) para criação e alteração de objetos/bancos de dados.

Liberação de direitos para alteração do serviço de logon ou porta de conexão local (TCP/IP), caso necessário.

Rede e Firewall:

Liberação de tráfego local no Firewall do Windows para as portas de rede do SQL Server (Porta padrão 1433 e porta dinâmica/Browser 1434).

Liberação do protocolo TCP/IP e do serviço SQL Server Browser nas configurações do banco.

Extensão VS Code:

Permissão de execução da extensão SQL Server (mssql) no VS Code para conexões locais via localhost / .\SQLEXPRESS.

Abaixo seguem duas consultas simples que utilizaremos com os participantes para testar se as permissões de criação de banco e tabelas foram aplicadas com sucesso.

Agradeço desde já pela colaboração!

Atenciosamente,

[Seu Nome / Equipe de Treinamento]

Scripts T-SQL para Teste de Conexão e Permissões
Você pode disponibilizar estes dois comandos para os alunos executarem sequencialmente no VS Code (Ctrl + Shift + E).

Teste 1: Criar o Banco de Dados (Create Database)
SQL
-- 1. Criar o Banco de Dados de Teste
CREATE DATABASE DB_TesteVSCode;
GO

-- Validar se o banco foi criado com sucesso
SELECT name, create_date 
FROM sys.databases 
WHERE name = 'DB_TesteVSCode';
GO
Teste 2: Criar uma Tabela e Inserir Dados (Create Table)
SQL
-- 2. Usar o Banco de Dados Criado
USE DB_TesteVSCode;
GO

-- Criar Tabela Simples
CREATE TABLE Alunos (
    ID INT IDENTITY(1,1) PRIMARY KEY,
    Nome VARCHAR(100) NOT NULL,
    DataCadastro DATETIME DEFAULT GETDATE()
);
GO

-- Inserir um registro de teste
INSERT INTO Alunos (Nome) 
VALUES ('Participante Teste');
GO

-- Consultar o resultado para confirmar as permissões
SELECT * FROM Alunos;
GO