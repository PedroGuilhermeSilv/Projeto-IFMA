# Sistema de Seleção Simplificada de professores (Demanda DEAD/IFMA)
## Problematicação
- No departamento de EAD do IFMA é necessário a cada semestre fazer a seleção simplificada de professores para ministrarem as disciplinas do próximo semestre, conforme critérios baseado nos editais aprovados pela PROJUR.

## O sistema deverá conter:
- A base de dados deve criptografar a senha do usuário.
- A interface deve ser web, com o framework Django.
- Os usuários podem ser administradores, coordenador do curso, professores avaliadores e candidatos cadastrados com senha.
- Os administradores (funcionários da DEAD) configuram o processo de seleção, definindo: 
 se será interna (apenas para servidores IFMA) ou se
será externa (para servidores IFMA e externos ao IFMA);
- Cada tipo de processo, solicita dados comuns, tais como: rg, cpf, comprovante residência, disciplina do semestre, informações de comprovação de curriculum, a saber: experiência docente, titulação, etc; e também dados específicos, como por exemplo, liberação da chefia imediata
se servidor IFMA.
- Um comprovante de inscrição deve ser encaminhado ao email do
candidato;
- O sistema deve permitir a homologação das inscrições realizadas.

Equipe de desenvolvimento: Pedro Guilherme Silva Moura, Leanderson, Carlos Augusto.
