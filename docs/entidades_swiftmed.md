Entidades SwiftMed e suas relações e permissões: 

### **Usuário**

* id  
* nome  
* email  
* senha_hash  
* tipo (ADMIN | SECRETARIO | MEDICO | PACIENTE)  
* ativo (bool)

### **Paciente**

* usuario_id  
* cpf  
* telefone

### **Médico**

* usuario_id  
* crm  
* especialidade

### **Secretário**

* usuario_id

### **Consulta**

* id  
* paciente_id  
  medico_id  
* data_hora  
* status  
* criado_por  
* cancelado_por   
* cancelado_em

