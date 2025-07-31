#!/usr/bin/env python
# coding: utf-8

# # Como configurar/instalar/usar o `Windows via docker` no `Linux Ubuntu`
# 
# ## Resumo
# 
# Neste documento estão contidos os principais comandos e configurações para configurar/instalar/usar o `Windows via docker` no `Linux Ubuntu`.
# 
# ## _Abstract_
# 
# _This document contains the main commands and settings for configuring/installing/using the `Windows via docker` on `Linux Ubuntu`._
# 

# ## Descrição [2]
# 
# ### `Windows via docker`
# 
# O Windows via Docker refere-se à execução de contêineres do Windows em ambientes Docker. Isso permite que aplicativos baseados no Windows sejam empacotados, distribuídos e executados usando a tecnologia de contêineres, oferecendo portabilidade, isolamento e escalabilidade. Com o Docker, os desenvolvedores podem criar e testar aplicativos do Windows de forma consistente em diferentes ambientes, simplificando o processo de desenvolvimento e implantação de software.
# 
# ### `docker`
# 
# Docker é uma plataforma de código aberto que simplifica o processo de criação, implantação e execução de aplicativos em contêineres. Os contêineres permitem empacotar um aplicativo juntamente com suas dependências em uma unidade isolada, garantindo que ele seja executado de maneira consistente em qualquer ambiente. Com o Docker, os desenvolvedores podem criar ambientes de desenvolvimento replicáveis, implementar aplicativos de forma rápida e eficiente, e dimensionar facilmente aplicativos em ambientes de produção. Ele oferece uma maneira flexível e leve de encapsular aplicativos, facilitando a distribuição e a escalabilidade.
# 
# ### `remmina`
# 
# `Remmina` é um cliente de desktop remoto de código aberto que suporta vários protocolos, como `RDP`, `VNC`, `SSH`, `NX`, `XDMCP` e `SPICE`. Ele oferece uma interface intuitiva e fácil de usar para acessar e controlar sistemas remotos de forma segura. Com recursos avançados, como suporte a vários perfis de conexão, compartilhamento de área de trabalho e redimensionamento dinâmico, `Remmina` é uma ferramenta versátil para administradores de sistemas e usuários que precisam acessar máquinas remotas de maneira eficiente e conveniente.
# 

# ## 1. Como configurar/instalar/usar o `Windows via docker` no `Linux Ubuntu` [1][3]
# 
# Para configurar/instalar/usar o `Windows via docker` no `Linux Ubuntu`, você pode seguir estes passos:
# 
# 1. Abra o `Terminal Emulator`. Você pode fazer isso pressionando: `Ctrl + Alt + T`

# 2. Certifique-se de que seu sistema esteja limpo e atualizado.
# 
#     2.1 Limpar o `cache` do gerenciador de pacotes APT. Especificamente, ele remove todos os arquivos de pacotes (`.deb`) baixados pelo APT e armazenados em `/var/cache/apt/archives/`. Digite o seguinte comando: `sudo apt clean` 
#     
#     2.2 Remover pacotes `.deb` antigos ou duplicados do cache local. É útil para liberar espaço, pois remove apenas os pacotes que não podem mais ser baixados (ou seja, versões antigas de pacotes que foram atualizados). Digite o seguinte comando: `sudo apt autoclean`
# 
#     2.3 Remover pacotes que foram automaticamente instalados para satisfazer as dependências de outros pacotes e que não são mais necessários. Digite o seguinte comando: `sudo apt autoremove -y`
# 
#     2.4 Buscar as atualizações disponíveis para os pacotes que estão instalados em seu sistema. Digite o seguinte comando e pressione `Enter`: `sudo apt update -y`
# 
#     2.5 Para ver a lista de pacotes a serem atualizados, digite o seguinte comando e pressione `Enter`:  `sudo apt list --upgradable`
# 
#     2.6 Realmente atualizar os pacotes instalados para as suas versões mais recentes, com base na última vez que você executou `sudo apt update -y`. Digite o seguinte comando e pressione `Enter`: `sudo apt full-upgrade -y`
# 
#     2.7 Remover pacotes que foram automaticamente instalados para satisfazer as dependências de outros pacotes e que não são mais necessários. Digite o seguinte comando: `sudo apt autoremove -y`
# 
#     2.8 Remover pacotes `.deb` antigos ou duplicados do cache local. É útil para liberar espaço, pois remove apenas os pacotes que não podem mais ser baixados (ou seja, versões antigas de pacotes que foram atualizados). Digite o seguinte comando: `sudo apt autoclean`

# Para criar um passo a passo que combina as informações fornecidas anteriormente com as novas informações sobre como executar o `Windows` em um contêiner `Docker`, siga os passos abaixo:
# 
# ### 1.1 Instalação do `Docker`
# 
# 1. **Instale o `Docker`:** Certifique-se de ter o `Docker` instalado no seu sistema. Você pode seguir a documentação oficial do `Docker` para a instalação específica do seu sistema operacional.
# 

# ### 1.2 Preparação do Ambiente
# 
# 1. **Verifique o Suporte a `KVM`:** Antes de iniciar, certifique-se de que seu sistema suporta `KVM` (`Kernel-based Virtual Machine`) para aceleração. Use os comandos:
# 
#     ```
#     sudo apt install cpu-checker -y
#     sudo kvm-ok
#     ```
# 
#     Se receber uma mensagem indicando que a aceleração `KVM` pode ser usada, você está pronto para prosseguir. Caso contrário, verifique as configurações de virtualização na BIOS do seu sistema.
# 

# ### 1.4 Instalação do `Docker`
# 
# 1. **Instale o `Docker`:** Certifique-se de ter o `Docker` instalado no seu sistema. Você pode seguir a documentação oficial do `Docker` para a instalação específica do seu sistema operacional.
# 

# ###  1.5 Como eu seleciono uma versão do `Windows`
# 
# Por padrão, o `Windows 11` será instalado.
# 
# 1. Mas você pode adicionar a variável de ambiente `VERSION` ao seu arquivo de composição, para especificar uma versão alternativa do `Windows` a ser baixada:
# 
#     ```
#     environment:
#         VERSION: "win10"
#     ```
# 
#     Selecione entre os valores abaixo:
# 
# #### 1.5.1 Sistemas Operacionais (SO) convencionais
# 
# | Valor    | Descrição              | Fonte       | Transferência | Tamanho |
# |:--------:|:-----------------------|:------------|:--------------|:-------:|
# | `win11`  | Windows 11 Pro         | Microsoft   | Rápida        | 6.4 GB  |
# | `win10`  | Windows 10 Pro         | Microsoft   | Rápida        | 5.8 GB  |
# | `ltsc10` | Windows 10 LTSC        | Microsoft   | Rápida        | 4.6 GB  |
# | `win81`  | Windows 8.1 Pro        | Microsoft   | Rápida        | 4.2 GB  |
# | `win7`   | Windows 7 SP1          | Bob Pony    | Média         | 3.0 GB  |
# | `vista`  | Windows Vista SP2      | Bob Pony    | Média         | 3.6 GB  |
# | `winxp`  | Windows XP SP3         | Bob Pony    | Média         | 0.6 GB  |
# 

# #### 1.5.2 Sistemas Operacionais (SO) para servidores
# 
# | Valor    | Descrição              | Fonte       | Transferência | Tamanho |
# |:--------:|:-----------------------|:------------|:--------------|:-------:|
# | `2022`   | Windows Server 2022    | Microsoft   | Rápida        | 4.7 GB  |
# | `2019`   | Windows Server 2019    | Microsoft   | Rápida        | 5.3 GB  |
# | `2016`   | Windows Server 2016    | Microsoft   | Rápida        | 6.5 GB  |
# | `2012`   | Windows Server 2012 R2 | Microsoft   | Rápida        | 4.3 GB  |
# | `2008`   | Windows Server 2008 R2 | Microsoft   | Rápida        | 3.0 GB  |
# 

# #### 1.5.3 Sistemas Operacionais (SO) personalizados
# 
# | Valor    | Descrição              | Fonte       | Transferência | Tamanho |
# |:--------:|:-----------------------|:------------|:--------------|:-------:|
# | `core11` | Tiny 11 Core           | Archive.org | Lenta         | 2.1 GB  |
# | `tiny11` | Tiny 11                | Archive.org | Lenta         | 3.8 GB  |
# | `tiny10` | Tiny 10                | Archive.org | Lenta         | 3.6 GB  |
# 

# ### 1.6 Configuração do Contêiner do `Windows`
# 
# 1. Na sua `/home/`, crie uma pasta para o seu repositório do Windows: `mkdir ~/windows-docker`
# 
# 2. Entre dentro do repositório `~/windows-docker/`, com o comando: `cd ~/windows-docker/`
# 
# 2. **Crie um arquivo chamado:** Dentro do repositório: `cd ~/windows-docker/`
# 
#   2.1 Crie o arquivo: `docker-compose.yml`, com o comando: `sudo nano docker-compose.yml`
# 
# 3. **Cole a configuração abaixo no arquivo:**
# 
#   ```
#   version: "3"
#   services:
#     windows:
#       image: dockurr/windows
#       container_name: windows
#       devices:
#         - /dev/kvm
#       cap_add:
#         - NET_ADMIN
#       ports:
#         - 8006:8006
#         - 3389:3389/tcp
#         - 3389:3389/udp
#       stop_grace_period: 2m
#       restart: on-failure
#       environment:
#         VERSION: "win10"
#         RAM_SIZE: "8G"
#         CPU_CORES: "4"
#         DISK_SIZE: "256G"
#       volumes:
#         - ./data:/storage/shared
#   ```
# 
# 4. **Personalização de Recursos:** Ajuste de RAM e CPUs: Para alterar os recursos padrão alocados, altere ou adicione ono final do arquivo `compose.yml` e com indentação as variáveis de ambiente `RAM_SIZE` e `CPU_CORES` ao seu arquivo `docker-compose.yml`:
# 
#   ```
#   environment:
#     RAM_SIZE: "8G"
#     CPU_CORES: "4"
#   ```
# 
# 5. **Expansão do Disco:** Para aumentar o tamanho padrão do disco, use a variável `DISK_SIZE`, ou seja, altere ou adicione no final do arquivo `compose.yml` e com indentação o código abaixo:
# 
#   ```
#   DISK_SIZE: "256G"
#   ```
# 
# 6. **Criar uma sessão chamada `volumes` para compartilhamento:** Para criar um volume para compartilhamento entre os Sistemas Operacionais (SO's), altere ou adicione no final do arquivo `compose.yml` e com indentação o código abaixo:
# 
#   ```
#   volumes:
#     - ./data:/storage/shared
#   ```
# 
# 7. **Instalar o `Docker`:** `sudo apt install docker-compose -y`
# 
# 8. **Instalar o `Windows` baseado nas configurações do `docker compose`:** Digite o comando a seguir para instalar o `Windows`: `sudo docker-compose up -d`
# 
# 9. **Acesso ao Windows e consulta do download de instalação:** Acesso via Navegador: Inicie o contêiner e acesse `http://localhost:8006` usando seu navegador web. Você poderá visualizar a instalação do Windows e, eventualmente, a área de trabalho pronta para uso.
# 

# ### 1.1 Código completo para configurar/instalar/usar
# 
# Para configurar/instalar/usar o `Windows via docker` no `Linux Ubuntu` sem precisar digitar linha por linha, você pode seguir estas etapas:
# 
# 1. Abra o `Terminal Emulator`. Você pode fazer isso pressionando: `Ctrl + Alt + T`
# 
# 2. Digite o seguinte comando e pressione `Enter`:
# 
#     ```
#     sudo apt clean
#     sudo apt autoclean -y
#     sudo apt autoremove -y
#     sudo apt update -y
#     sudo apt uptoremove -y
#     sudo apt autoclean -y
#     sudo apt-add-repository ppa:Windows via docker-ppa-team/Windows via docker-next
#     sudo apt update -y
#     sudo apt install Windows via docker Windows via docker-plugin-rdp Windows via docker-plugin-secret -y
#     ```
# 

# ## 2. Encerrar o `Windows`
# 
# Encerrar um sistema operacional `Windows` que está rodando em um contêiner Docker é um pouco diferente de interagir com contêineres que executam aplicações mais simples ou serviços `Linux`. Aqui estão os passos gerais para gerenciar contêineres Docker, incluindo como encerrar um contêiner que executa o `Windows` sob o `Linux Ubuntu`:
# 
# 1. **Listar Contêineres Ativos**: Primeiro, você precisa identificar o contêiner que deseja encerrar. Abra o Terminal e digite o seguinte comando para listar todos os contêineres ativos: `sudo docker ps`
# 
#     1.1 Se o contêiner que você deseja encerrar não aparecer nessa lista, você pode listar todos os contêineres (ativos e inativos) com: `sudo docker ps -a`
# 
# 2. **Encerrar o Contêiner**: Uma vez que você tenha identificado o contêiner que deseja encerrar (note o `CONTAINER ID` ou `NAMES`), você pode usar o comando `docker stop` seguido pelo `ID` ou nome do contêiner. Por exemplo: `sudo docker stop <CONTAINER_ID_OU_NAME>`
# 
#     Substitua `<CONTAINER_ID_OU_NAME>` pelo `ID` ou nome real do contêiner. Isso enviará um sinal para o contêiner parar de executar.
# 
# 3. **(Opcional) Remover o Contêiner**: Se você deseja não apenas encerrar o contêiner mas também removê-lo completamente do seu sistema, você pode usar o comando `docker rm` após ter parado o contêiner: `sudo docker rm <CONTAINER_ID_OU_NAME>`
# 
# Isso removerá o contêiner parado, liberando espaço no sistema.
# 
# **Nota Importante**
# 
# Normalmente, contêineres `Docker` são usados para executar aplicações ou serviços específicos em sistemas operacionais baseados em `Linux` devido à natureza da virtualização baseada em processos do `Docker`. Executar uma instância completa do `Windows` em um contêiner `Docker` não é o cenário de uso comum ou recomendado, principalmente devido a restrições de licenciamento e limitações técnicas.
# 
# Se você está tentando gerenciar uma instância de `Windows` em um ambiente virtualizado sob o `Linux`, soluções como `VirtualBox`, `VMware`, ou `QEMU` podem ser mais adequadas e oferecer uma experiência mais completa e integrada para sistemas operacionais completos, incluindo suporte a interface gráfica e integração de dispositivos.
# 

# ### 2.1 Encerramento após Reinício do Sistema
# 
# Se o contêiner parece estar rodando automaticamente após o reinício do sistema, você deve verificar se há alguma configuração, como um serviço `systemd` ou uma configuração de reinício automático do `Docker` (`--restart=always`), que está fazendo com que o contêiner seja iniciado automaticamente. Você pode ajustar essas configurações conforme necessário para impedir a execução automática após o reinício.
# 
# Para verificar e ajustar o comportamento de reinício automático de contêineres Docker, assim como identificar se há serviços systemd configurados para iniciar contêineres, siga as etapas abaixo:
# 
# #### 2.1.1 Verificar Configurações de Reinício do `Docker`
# `
# 1. **Listar Contêineres com Suas Configurações de Reinício:** Para verificar as configurações de reinício de todos os contêineres, você pode usar o comando `docker inspect`. Primeiro, liste todos os contêineres (ativo e inativos) para obter seus IDs ou nomes: `docker ps -a`
# 
# 2. **Verificar a Política de Reinício de um Contêiner:** Use o comando `docker inspect` para verificar a política de reinício de um contêiner específico. Substitua <CONTAINER_ID_OU_NAME> pelo ID ou nome do contêiner: `docker inspect --format='{{ .HostConfig.RestartPolicy }}' <CONTAINER_ID_OU_NAME>`
# 
#     Isso mostrará a política de reinício configurada para o contêiner. Se o valor for `{"Name":"always","MaximumRetryCount":0}`, significa que o contêiner está configurado para reiniciar automaticamente.
# 
# #### 2.1.2 Alterar a Política de Reinício do Contêiner
# 
# 1. Se você deseja mudar a política de reinício de um contêiner para que ele não inicie automaticamente após o reinício do sistema, você pode usar o comando `docker update`. Por exemplo, para alterar a política de reinício para no, faça o seguinte: `docker update --restart=no <CONTAINER_ID_OU_NAME>`
# 
# 2. **Reverificar a Política de Reinício de um Contêiner:** Use o comando `docker inspect` para reverificar a política de reinício de um contêiner específico. Substitua <CONTAINER_ID_OU_NAME> pelo ID ou nome do contêiner: `docker inspect --format='{{ .HostConfig.RestartPolicy }}' <CONTAINER_ID_OU_NAME>`
# 
#     Isso mostrará a política de reinício configurada para o contêiner. Se o valor for `{on-failure 0}`, significa que o contêiner está configurado para reiniciar automaticamente.
# 
# #### 2.1.3 Verificar e Desabilitar Serviços `Systemd`
# 
# Se você suspeita que um serviço `systemd` está configurado para iniciar o Docker ou contêineres Docker automaticamente, você pode verificar e alterar essa configuração.
# 
# 1. **Listar Serviços Systemd do `Docker`**: Você pode listar todos os serviços `systemd` relacionados ao Docker com o comando: `systemctl list-unit-files | grep docker`
# 
# 2. **Verificar o Status de um Serviço**: Para verificar o status de um serviço específico do `Docker`, use: `systemctl status <nome_do_serviço>.service`
# 
#     Substitua <nome_do_serviço>.service pelo nome do serviço que você identificou e deseja verificar.
# 
# 3. **Desabilitar um Serviço**: Se você encontrar um serviço que não deseja que inicie automaticamente, você pode desabilitá-lo usando: `systemctl disable <nome_do_serviço>.service`
# 
#     Isso impedirá que o serviço inicie automaticamente no `boot`.
# 
# Estas etapas devem ajudá-lo a gerenciar e ajustar o comportamento de reinício automático dos seus contêineres `Docker` e de qualquer serviço `systemd` relacionado. É importante garantir que apenas os serviços e contêineres desejados sejam configurados para iniciar automaticamente, mantendo o controle sobre o ambiente de execução.

# ## 3. Instalação do `Remmina`
# 
# Conexão `RDP` para Melhor Experiência: Para uma qualidade superior de imagem e som, conecte-se usando qualquer cliente de Área de Trabalho Remota da Microsoft ao IP do contêiner, utilizando o nome de usuário `docker` e sem senha.
# 
# 1. **Instale o `Remmina`:** Certifique-se de ter o Remmina instalado no seu sistema. Você pode seguir a documentação oficial do Remmina para a instalação específica do seu sistema operacional.

# ## 4. Compartilhamento de Arquivos e Armazenamento Personalizado
# 
# 1. **Compartilhamento de Arquivos com o Host**: Acesse o Explorador de Arquivos do `Windows` e navegue até a seção de Rede para encontrar e usar a pasta compartilhada Data.
# Local de Armazenamento Personalizado: Para modificar o local de armazenamento padrão, inclua um mapeamento de volume no seu arquivo `docker-compose.yml`.
# 
# 2. **Instalação de Imagem Personalizada do Windows
# Uso de Imagem ISO Customizada**: Para usar uma imagem ISO personalizada do Windows, defina a variável VERSION com a URL da ISO ou renomeie um arquivo local para custom.iso e coloque-o no diretório `/storage`.
# 
# **Conclusão**: Após a conclusão da instalação automática, você terá uma instalação do Windows pronta para uso dentro de um contêiner `Docker`. Aproveite sua nova máquina e não esqueça de explorar mais configurações conforme necessário.
# 
# Este guia fornece um caminho detalhado e simplificado para executar o Windows em um ambiente `Docker`, aproveitando a facilidade de uso e flexibilidade que essa abordagem oferece.

# ## Referências
# 
# [1] OPENAI. ***Instalar Windows via docker no Ubuntu.*** Disponível em: <https://chat.openai.com/c/586f8f0a-8543-4d9f-9f60-98a2fb51a611> (texto adaptado). Acessado em: 05/04/2023 17:11.
# 
# [2] OPENAI. ***Vs code: editor popular.*** Disponível em: <https://chat.openai.com/c/b640a25d-f8e3-4922-8a3b-ed74a2657e42> (texto adaptado). Acessado em: 05/04/2024 17:10.
# 
