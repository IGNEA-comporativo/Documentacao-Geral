# Contabo — Guia de Uso da Plataforma

Guia para operar as VPS da **Contabo** usadas pelos projetos da equipe. Foca em **como acessar**, **onde encontrar** cada projeto e **o que fazer no dia a dia** pelo **painel Contabo** e por **SSH** quando necessário.

> Para detalhes finos de execução/rotina de cada projeto, consulte a documentação do respectivo sistema.

---

## O que está em execução

Temos **duas VPS separadas**, uma para cada projeto (referenciadas pelo **nome do projeto**):

| Projeto | VPS/Identificação no painel | IP | Diretório principal | Serviço (`systemd`) | Repositório |
|---|---|---|---|---|---|
| Monitoramento de Processos | vmi2694728 | 213.199.39.53 | `/root/ANMScrapping` | `myscraper.service` | https://github.com/IGNEA-comporativo/CadastroMineiroScrapping |
| Workana (projeto de terceiro) | vmi2713330 | 212.90.121.173 | _a confirmar_ | _a confirmar_ | https://github.com/IGNEA-comporativo/anm_api |

---

## Acesso ao painel Contabo

- **Como acessar**: utilize o **painel da Contabo** pela [nova versão](https://new.contabo.com/servers/vps), ou pela [versão legacy](https://my.contabo.com/abos#),  com as **credenciais disponíveis no Discord**.
- **O que você encontra no painel**:
  - **Lista de VPS** com status e recursos.
  - **Ações rápidas**: reiniciar/desligar/ligar a VPS.
  - **Console remoto (NoVNC)** para acesso emergencial.
  - **Rede e IP público** (visualização).
  - **Histórico de atividades básicas da instância**.

---

## Acesso por SSH

- **Usuário**: `root`  
- **Autenticação**: **senha** disponível no **Discord**  
- **Host**: use o **IP público** exibido no painel Contabo (e também no discord)

---

## Operar os projetos (visão prática)

### 1) Monitoramento de Processos
- **Diretório**: `/root/ANMScrapping`  

- **Serviço**: `myscraper.service` (gerencia a execução contínua).  
- **Como operar**: utilize os **alvos do `Makefile`** e os passos descritos na [documentação do sistema](https://github.com/IGNEA-comporativo/CadastroMineiroScrapping)(reiniciar serviço, verificar status, inspecionar logs, etc.).  
  - Para entendimento do fluxo e rotinas, consulte: **Documentação do Monitoramento de Processos** (neste repositório) e o repositório do projeto:  
    - GitHub: https://github.com/IGNEA-comporativo/CadastroMineiroScrapping

### 2) Workana
- Projeto desenvolvido por **terceiro contratado via Workana**.  
- **Mais informações são necessárias** para operação detalhada (diretório, serviço, comandos).  
- Repositório: https://github.com/IGNEA-comporativo/anm_api


---

## Diagrama simples (o que gerenciamos na Contabo)

```{mermaid}
flowchart LR
    C[Contabo - Painel] --> V1[VPS - Monitoramento de Processos]
    C --> V2[VPS - Workana]
    V1 --> D1[/ /root/ANMScrapping /]
    D1 --> S1[Serviço systemd: myscraper.service]
    V2 --> D2[/ diretório a confirmar /]
    D2 --> S2[Serviço a confirmar]
```

---

## Migração obrigatória para AWS (Lightsail/EC2)

```{warning}
Todos os sistemas atualmente hospedados na **Contabo** devem ser **transicionados para a AWS**, preferencialmente como **contêiner** em **Lightsail** (quando for “VPS-like”) ou **EC2** (quando exigir maior flexibilidade). Essa mudança é **prioritária** por padronização, segurança, escalabilidade e governança de custos.
```

**Novos serviços**: já nascer na **AWS** (não criar nada novo na Contabo).
