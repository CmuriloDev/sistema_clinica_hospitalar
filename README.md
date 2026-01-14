# 🏥 SwiftMed

Sistema desenvolvido em Python e Flask com foco em boas práticas de arquitetura, separação de responsabilidades e evolução incremental.  
O objetivo do projeto é ser um sistema de agendamento médico.

## 🎯 Objetivo do Projeto

Criar um sistema de agendamento de consultas, contendo:
- Cadastro de pacientes e médicos
- Agendamento e cancelamento de consultas
- Validação de conflitos de horário
- Diferentes tipos de usuários (em planejamento)
- Interface Web
- Persistência em banco de dados

---

## 🧠 Arquitetura

O sistema segue uma separação clara entre:
- **Models**: entidades do domínio (Paciente, Médico, Consulta)
- **Regras de negócio**: validações e operações do sistema
- **Interface**: inicialmente em terminal, com migração planejada para Web
- **Persistência**: atualmente em memória, com migração planejada para banco de dados

---

## ⚙️ Funcionalidades Atuais

- Cadastro de pacientes
- Cadastro de médicos
- Listagem de pacientes e médicos
- Agendamento de consultas
  - Validação de datas e horários
  - Impede agendamento em datas passadas
  - Impede conflitos de horário para o mesmo médico
- Cancelamento de consultas com validação de status

---

## 🚧 Funcionalidades em Desenvolvimento

- Interface Web
- Persistência em banco de dados (Firebase)
- Sistema de usuários (admin, médico, paciente)
- Controle de permissões
- Histórico de consultas
- Testes automatizados

---

## 🛠️ Tecnologias Utilizadas

- Python
- Programação Orientada a Objetos
- (Em breve) Flask ou FastAPI
- (Em Breve) Firebase

---

## 📌 Status do Projeto

🟡 Em desenvolvimento ativo  
O projeto está sendo evoluído incrementalmente com commits frequentes.

---

## 👨‍💻 Autor

Desenvolvido por **Carlos Murilo**  
Estudante de Engenharia de Software, com foco em backend, arquitetura e sistemas inteligentes.
