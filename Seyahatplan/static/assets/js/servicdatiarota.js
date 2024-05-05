<script>
  document.addEventListener('DOMContentLoaded', function() {
    document.querySelectorAll('.rota-link').forEach(link => {
      link.addEventListener('click', function(event) {
        event.preventDefault(); // Sayfanın yeniden yüklenmesini engelle
        const targetId = this.getAttribute('href').substring(1); // Linkin href özelliğinden hedef ID'yi al
        const targetElement = document.getElementById(targetId); // Hedef ID'ye sahip elementi bul
        if (targetElement) {
          targetElement.scrollIntoView({ behavior: 'smooth', block: 'start' }); // Hedef elemente yumuşak bir şekilde kaydır
        }
      });
    })
  });
</script>
