// Pega o botão
var meuBotao = document.getElementById("btnVoltarTopo");

// Quando o usuário rolar a página, execute a função scrollFunction
window.onscroll = function() {scrollFunction()};

function scrollFunction() {
  // Se a rolagem vertical for maior que 20px, mostre o botão, senão esconda-o
  if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
    meuBotao.style.display = "block";
  } else {
    meuBotao.style.display = "none";
  }
}

// Quando o usuário clicar no botão, volte ao topo do documento
function voltarAoTopo() {
  document.body.scrollTop = 0; // Para navegadores Safari
  document.documentElement.scrollTop = 0; // Para Chrome, Firefox, IE e Opera
}