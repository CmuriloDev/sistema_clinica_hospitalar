# **📘 Regras de Negócio**

**SwiftMed**

## **1\. Visão Geral**

Este documento descreve as **regras de negócio** do sistema de agendamento de consultas médicas.  
 O objetivo é garantir **consistência**, **segurança operacional** e **controle de acesso**, evitando conflitos de agenda, uso indevido do sistema e inconsistências de dados.

---

## **2\. Perfis de Usuário **

O sistema possui os seguintes perfis:

### **2.1 Admin**

* Perfil com **acesso total ao sistema**

* Responsável por configurações globais e gestão completa

### **2.2 Secretário**

* Perfil operacional

* Responsável pelo fluxo de agendamentos da clínica

### **2.3 Médico**

* Perfil clínico

* Acesso restrito às próprias consultas

### **2.4 Paciente**

* Perfil de autoatendimento

* Acesso apenas às próprias informações e consultas

---

## **3\. Permissões por Funcionalidade**

### **3.1 Agendar Consulta**

**Permissão:**

* Secretário

* Admin

**Restrições:**

* A consulta só pode ser criada se:

  * O paciente estiver cadastrado

  * O médico estiver cadastrado

  * Não existir outra consulta para o mesmo médico no mesmo horário

  * A data e hora forem futura
 
  * Ter um tempo mínimo de 20 minutos após uma consulta já agendada de um mesmo médico

* Pacientes **não podem agendar consultas diretamente**, para evitar uso indevido do sistema

---

### **3.2 Cancelar Consulta**

**Permissão:**

* Secretário

* Admin

**Restrições:**

* A consulta só pode ser cancelada se o status for **"Agendada"**

* Consultas com status:

  * `"Cancelada"`

  * `"Finalizada"`

* **não podem ser alteradas**

---

### **3.3 Visualizar Consultas por Paciente (CPF)**

**Permissão:**

* Secretário

* Admin

* Paciente

**Restrições:**

* O paciente só pode visualizar **as próprias consultas**

* Secretário e Admin podem visualizar consultas de qualquer paciente

---

### **3.4 Visualizar Consultas por Médico (CRM)**

**Permissão:**

* Secretário

* Admin

* Médico

**Restrições:**

* O médico só pode visualizar **as próprias consultas**

* Secretário e Admin podem visualizar consultas de qualquer médico

---

### **3.5 Listar Todas as Consultas da Clínica**

**Permissão:**

* Secretário

* Admin

**Restrições:**

* Nenhuma

---

### **3.6 Cadastrar Médico**

**Permissão:**

* Secretário

* Admin

**Restrições:**

* CRM deve ser único

* Médico **não pode se cadastrar sozinho**, evitando registros inválidos

---

### **3.7 Cadastrar Paciente**

**Permissão:**

* Secretário

* Admin

* Paciente

**Restrições:**

* CPF deve ser único

* Dados obrigatórios:

  * Nome

  * CPF
 
  * Telefone

  * E-mail

---

## **4\. Regras de Datas e Horários**

* O sistema **não permite consultas em datas ou horários passados**

* Datas e horários devem seguir o formato:

  * Data: `DD/MM/YYYY`

  * Hora: `HH:MM`

* O sistema impede:

  * Dois agendamentos para o **mesmo médico no mesmo horário**
  * Agendamentos com horários muito próximos de um mesmo médico

---

## **5\. Status de Consulta**

Uma consulta pode possuir apenas um dos seguintes status, mas futuramente serão implementados mais opções:

* `"Agendada"`

* `"Cancelada"`

* `"Finalizada"`

### **Regras:**

* Apenas consultas **Agendadas** podem ser canceladas

* Consultas **Finalizadas** são imutáveis

* Status não deve ser tratado como string livre no futuro (uso de Enum futuramente)

---

## **6\. Integridade e Evolução do Sistema**

* As regras de negócio são independentes da interface (CLI, Web)

* A persistência em banco de dados (Firebase) deve respeitar todas as validações aqui descritas

* Este documento serve como base para:

  * Backend

  * API

  * Testes

  * Auditoria do sistema

