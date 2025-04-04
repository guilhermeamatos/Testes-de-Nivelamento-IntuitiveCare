<template>
  <div class="search-container">
    <h1>Buscar por Operadora</h1>

    <div class="search-bar">
      <input
        v-model="searchTerm"
        @keyup.enter="search"
        placeholder="Digite o valor de busca"
      />
      <button @click="search">Buscar</button>
    </div>

    <div
      v-for="(operadora, index) in operadoras"
      :key="index"
      class="operadora"
      @click="toggleInfo(index)"
    >
      <h2>{{ operadora.Razao_Social }}</h2>

      <div v-if="showInfoIndex === index" class="detalhes-operadora">
        <div class="info-bloco">
          <h3>📞 Contato</h3>
          <p><strong>Telefone:</strong> {{ operadora.Telefone }} ({{ operadora.DDD }})</p>
          <p><strong>Fax:</strong> {{ operadora.Fax || 'Não informado' }}</p>
          <p><strong>Email:</strong> {{ operadora.Endereco_eletronico }}</p>
          <p><strong>Representante:</strong> {{ operadora.Representante }} ({{ operadora.Cargo_Representante }})</p>
        </div>

        <div class="info-bloco">
          <h3>🏠 Endereço</h3>
          <p><strong>Logradouro:</strong> {{ operadora.Logradouro }}</p>
          <p><strong>Número:</strong> {{ operadora.Numero }}</p>
          <p><strong>Complemento:</strong> {{ operadora.Complemento }}</p>
          <p><strong>Bairro:</strong> {{ operadora.Bairro }}</p>
          <p><strong>Cidade:</strong> {{ operadora.Cidade }} - {{ operadora.UF }}</p>
          <p><strong>CEP:</strong> {{ operadora.CEP }}</p>
        </div>

        <div class="info-bloco">
          <h3>📄 Informações Adicionais</h3>
          <p><strong>CNPJ:</strong> {{ operadora.CNPJ }}</p>
          <p><strong>Modalidade:</strong> {{ operadora.Modalidade }}</p>
          <p><strong>Registro ANS:</strong> {{ operadora.Registro_ANS }}</p>
          <p><strong>Data Registro ANS:</strong> {{ operadora.Data_Registro_ANS }}</p>
          <p><strong>Região Comercialização:</strong> {{ operadora.Regiao_de_Comercializacao }}</p>
        </div>
      </div>
    </div>

    
    <div v-if="erro" class="error-message">
      {{ erro }}
    </div>
  </div>
</template>

<script>
import { ref } from 'vue';

export default {
  name: 'SearchOperadoras',
  setup() {
    const searchTerm = ref('');
    const operadoras = ref([]);
    const showInfoIndex = ref(null);
    const erro = ref('');

    const search = async () => {
      erro.value = '';
      operadoras.value = [];

      try {
        const response = await fetch(`http://127.0.0.1:5000/search?q=${searchTerm.value}`);
        const rawText = await response.text();
        const data = JSON.parse(rawText);
        operadoras.value = data;
      } catch (error) {
        console.error('Erro ao buscar operadoras:', error);
        erro.value = 'Ocorreu um erro ao buscar operadoras.';
      }
    };

    const toggleInfo = (index) => {
      showInfoIndex.value = showInfoIndex.value === index ? null : index;
    };

    return {
      searchTerm,
      operadoras,
      showInfoIndex,
      erro,
      search,
      toggleInfo,
    };
  },
};
</script>

<style scoped>
html, body {
  margin: 0;
  padding: 0;
  overflow-x: hidden;
}

*, *::before, *::after {
  box-sizing: border-box;
}

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600&display=swap');

.search-container {
  background-color: #f9fafa;
  border-radius: 12px;
  padding: 2rem;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.05);
  max-width: 700px;
  width: 100%;
  margin: 2rem auto;
}

.search-container h1 {
  text-align: center;
  margin-bottom: 1.5rem;
  color: #333;
}

.search-bar {
  display: flex;
  gap: 0.75rem;
  width: 100%;
  margin-bottom: 2rem;
}

.search-bar input {
  flex: 1;
  padding: 0.75rem;
  border: 1px solid #ccc;
  border-radius: 8px;
  font-size: 1rem;
}

.search-bar button {
  padding: 0.75rem 1.5rem;
  background-color: #4caf50;
  color: white;
  font-weight: 600;
  border: none;
  border-radius: 8px;
  cursor: pointer;
  transition: background 0.3s;
  font-size: 1rem;
}

.search-bar button:hover {
  background-color: #45a049;
}

.operadora {
  background-color: #ffffff;
  border-radius: 10px;
  padding: 1rem;
  margin-bottom: 1.5rem;
  box-shadow: 0 2px 6px rgba(0, 0, 0, 0.05);
  cursor: pointer;
  transition: box-shadow 0.2s;
}

.operadora:hover {
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
}

.operadora h2 {
  color: #2c3e50;
  font-size: 1.2rem;
  margin-bottom: 0.5rem;
}

.detalhes-operadora {
  margin-top: 1rem;
  line-height: 1.6;
  font-size: 0.95rem;
}

.info-bloco {
  margin-bottom: 1rem;
  background: #f5f7f9;
  border-radius: 6px;
  padding: 0.75rem;
}

.info-bloco h3 {
  margin-bottom: 0.5rem;
  font-size: 1rem;
  color: #444;
}

.error-message {
  margin-top: 1rem;
  color: red;
  font-weight: bold;
  text-align: center;
}
@media (max-width: 700px) {
  .search-container {
    max-width: 95%;
    padding: 1rem;
    margin: 1rem auto;
  }
}
</style>
