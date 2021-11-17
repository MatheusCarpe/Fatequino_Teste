from setuptools import setup
description = 'Os programas deste pacote foram adaptados para rodar diretamente no Raspberry Pi 3 do projeto fatequino e, portanto, os paths'\
              'de referência dos arquivos de dados estão vinculados ao usuário pi do sistema Raspbian' \
'Estes programas também foram testados no ambiente Windows e, neste caso, é necessário criar pastas com a mesma estrutura.' \
'Em ambos os casos a pasta raiz usada é a Desktop.' \
'Obs: No Raspberry Pi a pasta Desktop é a área de trabalho do usuário pi mas no Windows é apenas uma pasta comum.' \
'Pasta de imagens:' \
'Os programas foram adaptados para gravar e ler imagens na seguinte pasta:' \
'No Raspberry Pi:' \
'home pi Desktop reconhecimento Data' \
'No Windows:' \
'C: home pi Desktop reconhecimento Data' \
'Programas:' \
'1) capturandoRosto.py' \
'Este programa pede a identificação do aluno, pode ser um nome (não deve conter espaços, barras, ou caracteres estranos) ou o RA do aluno, e cria uma subpasta com essa identificação dentro da pasta de imagens.' \
'Ativa a câmera do Raspberry Pi exibe um quadro de tamanho reduzido na tela, localiza um rosto' \
'humano baseado em um modelo padrão haarcascade_frontalface_alt.xml  contido na pasta do projeto e captura automaticamente' \
'até 50 imagens do rosto do aluno fazendo um recorte de tamanho padrão de 150 por 150 pixels e adaptando o tamanho para poder' \
'fazer a análise comparativa de imagens posterior. ' \
'O aluno pode movimentar-se naturalmente em frente á câmera durante o processo de captura para que o sistema tenha' \
'diversas imagens ligeiramente diferentes do mesmo rosto e possa criar um banco de dados com essas imagens.' \
'Um contador de imagens capturadas é exibida no topo da tela que mostra o rosto do aluno durante o processo. Caso não queira' \
'esperar a captura das 50 imagens o usuário pode teclar ESC (se houver teclado anexado) e abortar o programa.' \
'Pode-se reiniciar o processo posteriormente fornecendo a mesma identificação do aluno dada inicialmente e as novas imagens' \
'capturadas serão anexadas aquelas já existentes na pasta de imagens.' \
'Obs 1: No Windows a ativação da câmera, geralmente plugada via porta USB, pode requerer um parâmetro complementar no comando' \
'de ativaçãoo da câmera. Por este motivo foi usado nos programas a biblioteca platform que permite identificar se o programa' \
'está sendo executado no Windows para usar este parâmetro adicional.' \
'2) treinandoRF.py' \
'Este programa irá processar todas as imagens contidas na pasta de imagens do sistema e irá gerar um arquivo de parametrização' \
'modeloLBPHFace.xml que será usado no terceiro programa que faz o reconhecimento facial. ' \
'Foi escolhido o método LBPHFaceRecognizer Local Binary Patterns Histograms usado na biblioteca complementar do OpenCV' \
'chamada opencv-contrib-python.' \
'Após o treinamento o programa deverá gerar o arquivo XML com os parâmetros de reconhecimento ajustados' \
'para aquele conjunto de imagens. Obs: não misturar na mesma subpasta de imagens de um aluno fotos de outros alunos.' \
'3) ReconhecimentoFacial.py' \
'Este programa irá ativar a câmera do Raspberry Pi exibe um quadro de tamanho reduzido na ela,' \
'localiza um rosto humano baseado em um modelo padrão haarcascade_frontalface_alt.xml  e usa' \
'o método LBPHFaceRecognizer com o arquivo de modelos gerado pelo programa de treinamento' \
'modeloLBPHFace.xml para obter a identificação provável de um rosto capturado pela câmera. Ao encontrar um ID sequencial' \
'contido nesse arquivo de parâmetros ele busca, pela ordem, o nome da pasta de imagens que corresponde ao ID encontrado e' \
'desenha um quadro ao redor do rosto que aparece na imagem da câmera e imprime a identificação do usuário no alto desse quadro. ' \
'4) HandGestureV(n).py' \
'Estão disponibilizados nesta edição do projeto 2 versões do programa de reconhecimento de gestos das mãos.' \
'A primeira versão HandGestureV3.py é apenas uma correção do programa publicado pelas equipes anteriores para poder rodar,' \
'relativamente sem erros de execução e com um pouco mais de velocidade, no ambiente do Raspberry Pi pois este programa,' \
'originalmente, foi desenvolvidor fora do ambiente deste equipamento provavelmente num PC e continha chamadas para exibição' \
'de telas de depuração de imagens e gravação de um arquivo de video  que deixavam a aplicação mais lenta. ' \
'Além disso, foi incluído um bloco de tratamento de excessões pois, em determinadas situações, a biblioteca de reconhecimento' \
'de padrões usada gerava um erro interno que parava o programa completamente.' \
'Embora tenha havido alguma melhora e permita executar este programa no Raspberry Pi o modelo usado neste programa (V3) tenta' \
'inferir o contorno da mão e ângulos entre os dedos usando um método que é altamente dependente de iluminação adequada e' \
'pode confundir outros elementos do ambiente como fazendo parte da análise. Gera muitos falsos positivos e erros de' \
'identificação com resultados imprevisíveis.' \
'Dados os problemas relatados na versão V3 foi criada uma nova versão (V4) com uma abordagem totalmente diferente da anterior' \
'e que utiliza a biblioteca mediapipe (Google) com um algoritmo baseado no TensorFlow que consegue extrair das imagens a' \
'posição exata de cada dedo das mãos que permitiria até criar um modelo 3D se necessário.' \
'A biblioteca mediapipe foi instalada no Raspberry Pi e nos testes realizados diretamente no equipamento conseguiu ler' \
'com precisão a posição de todos os dedos da mão. Entretanto, devido ao equipamento ser de reduzido poder de processamento,' \
'a velocidade de reconhecimento ficou reduzida a 1 frame por segundo mas, mesmo assim, sem erros devido a presença de outros' \
'elementos visuais na imagem e com baixa iluminação.' \
'Foram acrescentados neste programa rotinas que permitem identificar a posição de apenas 1 dedo (se necessário) ou de vários' \
'(ou todos) de uma mão ou até duas ao mesmo tempo. A posição dos dedos é desenhada virtualmente sobre a imagem da câmera' \
'permitindo mostrar em destaque a posição de cada ponto de referência (4 por dedo e 1 na base da mão) com cores diferentes.' \
'Esta versão ainda está em desenvolvimento para permitir calcular os ângulos dos dedos (em relação á base da imagem e entre os dedos) e, eventualmente, determinar se estão abertos, fechados, curvados, etc. Entretanto, até essa versão, não foi' \
'criado um dicionário de posições que permite, por exemplo, obter uma letra da linguagem brasileira de sinais (libras) mas' \
'com as funções implementadas até o momento isso será plenamente possível numa futura versão.' \
'5) Faces.py' \
'Este é um programa exemplo de uma possível interface visual que pode ser implementada no Fatequino (futuramente) no qual,' \
'usando-se um display de LCD acoplado no equipamento, é exibido um par de olhos que ficam piscando quando o equipamento,' \
'através da câmera, consegue encontrar um rosto nas imagens capturadas e, ao identificar um aluno, � exibida sua ' \
'identificação no alto da tela. ' \
'Foram reunidos, num código só, rotinas que desenham olhos (com base em imagens que estão na subpasta imagens) em várias' \
'posições (abertos, cerrados, fechados, piscando) e os programas de captura de rostro (item 1) que localiza nas imagens da câmera um rosto genérico e, neste caso, mostra os olhos em posições cerrada (como se estivesse tentando reconhecer alguém)' \
'e o programa de reconhecimento facial (item 3) que, quando consegue encontrar um ID correspondente ao rosto, pisca um dos' \
'olhos e exibe no alto da tela a identificação do aluno. Os olhos ficam piscando na tela de tempos em tempos como acontece' \
'com uma pessoa mostrando que o programa está em funcionamento normal e gerando uma maior empatia com o usuário.' \
'Além disso, caso as imagens do aluno estejam na pasta com nome especial chamada DEMO durante o processo de treinamento, ' \
'será exibida uma figura de fundo com uma imagem de terror (zumbi). Isso é um exemplo de uma aplicaçao lúdica que pode ser' \
'criada acoplando-se um display no Fatequino e permita uma maior interação com o usuário.' \
'Pode-se também aprimorar essa interface gráfica com um rosto e com acesso, pela internet, a outros dados relativos ao' \
'aluno identificado exibindo-se, em forma adequada, tais informações na tela tornando o projeto mais interativo e simpático ao ser humano.'

setup(
    name = 'fatequino_robotic_vision',
    version = '1.0.0',
    author = 'Visão - FATEC - 6o sem ADS Noturno',
    author_email = 'matheus.silva263@fatec.sp.gov.br',
    description = 'Este código é responsavel pela estrutura de visão robótica.',
    long_description= description,
    license = 'MIT',
    url = 'https://github.com/MatheusCarpe/Fatequino-robotic-vision',
    keywords = ['VISAO', 'FATEC', 'PROFESSORES', 'TURMAS'],
    classifiers = [
      'Development Status :: 4 - Beta',
      'Natural Language :: Portuguese (Brazilian)',
      'License :: OSI Approved :: MIT License',
      'Intended Audience :: Education'
    ]
)

