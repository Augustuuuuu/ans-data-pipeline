<script setup>
import { ref, watch } from 'vue'
import axios from 'axios'

const searchQuery = ref('')
const searchField = ref('all')
const results = ref([])
const loading = ref(false)
const error = ref(null)
let debounceTimer = null

const formatCNPJ = (cnpj) => {
  if (!cnpj) return '-'
  return cnpj.replace(/(\d{2})(\d{3})(\d{3})(\d{4})(\d{2})/, '$1.$2.$3/$4-$5')
}

const formatPhone = (ddd, phone) => {
  if (!ddd || !phone) return '-'
  return `(${ddd}) ${phone}`
}

const performSearch = async () => {
  if (debounceTimer) {
    clearTimeout(debounceTimer)
  }
  
  debounceTimer = setTimeout(async () => {
    if (searchQuery.value.trim() === '') {
      results.value = []
      error.value = null
      return
    }
    
    loading.value = true
    error.value = null
    
    try {
      const url = `http://localhost:5000/api/search?q=${encodeURIComponent(searchQuery.value)}&field=${searchField.value}`
      const response = await axios.get(url)
      results.value = response.data
    } catch (err) {
      console.error('Erro na busca:', err)
      error.value = 'Erro ao realizar a busca. Tente novamente.'
      results.value = []
    } finally {
      loading.value = false
    }
  }, 500) // Aumentando o debounce para 500ms
}

// Observar mudanças no campo de busca
watch([searchQuery, searchField], () => {
  performSearch()
})
</script>

<template>
  <div class="app-container">
    <div class="content-wrapper">
      <h1 class="title">Busca de Operadoras de Saúde</h1>

      <!-- Campo de Busca -->
      <div class="search-container">
        <div class="input-group search-group">
          <input 
            type="text" 
            class="form-control search-input" 
            v-model="searchQuery" 
            placeholder="Digite sua busca..."
          >
          <select class="form-select" v-model="searchField">
            <option value="all">Todos os Campos</option>
            <option value="Razao_Social">Razão Social</option>
            <option value="CNPJ">CNPJ</option>
            <option value="Nome_Fantasia">Nome Fantasia</option>
            <option value="Modalidade">Modalidade</option>
            <option value="Cidade">Cidade</option>
            <option value="UF">Estado</option>
            <option value="Telefone">Telefone</option>
            <option value="Representante">Representante</option>
          </select>
        </div>
        <div v-if="searchQuery && !loading" class="results-count-above">
          {{ results.length }} resultado{{ results.length !== 1 ? 's' : '' }} encontrado{{ results.length !== 1 ? 's' : '' }}
        </div>
      </div>

      <!-- Mensagens de Status -->
      <div v-if="error" class="alert alert-danger">
        {{ error }}
      </div>

      <!-- Resultados -->
      <div class="results-container">
        <div v-if="loading" class="loading-container">
          <div class="spinner-border text-light" role="status">
            <span class="visually-hidden">Carregando...</span>
          </div>
        </div>
        <div v-else>
          <div v-if="results.length === 0 && searchQuery" class="alert alert-info">
            Nenhum resultado encontrado.
          </div>
          <div v-else-if="results.length > 0">
            <div class="table-responsive">
              <table class="table table-dark table-striped table-hover">
                <thead>
                  <tr>
                    <th>Razão Social</th>
                    <th>Nome Fantasia</th>
                    <th>CNPJ</th>
                    <th>Modalidade</th>
                    <th>Cidade/UF</th>
                    <th>Telefone</th>
                    <th>Representante</th>
                  </tr>
                </thead>
                <tbody>
                  <tr v-for="result in results" :key="result.CNPJ">
                    <td class="razao-social">{{ result.Razao_Social }}</td>
                    <td class="nome-fantasia">{{ result.Nome_Fantasia || '-' }}</td>
                    <td class="cnpj">{{ formatCNPJ(result.CNPJ) }}</td>
                    <td class="modalidade">{{ result.Modalidade }}</td>
                    <td class="localizacao">{{ result.Cidade }}/{{ result.UF }}</td>
                    <td class="telefone">{{ formatPhone(result.DDD, result.Telefone) }}</td>
                    <td class="representante">{{ result.Representante || '-' }}</td>
                  </tr>
                </tbody>
              </table>
            </div>
            <div class="results-count">
              Total de resultados: {{ results.length }}
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style>
/* Centralização total da página */
.app-container {
  min-height: 100vh;
  width: 100%;
  background-color: #131313;
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 0;
  margin: 0;
}

/* Wrapper do conteúdo */
.content-wrapper {
  width: 100%;
  min-height: 100vh;
  background-color: #1e1e1e;
  border-radius: 0;
  padding: 2rem;
  box-shadow: none;
  display: flex;
  flex-direction: column;
  align-items: center;
  overflow-y: auto;
}

/* Título */
.title {
  font-size: 2.2rem;
  font-weight: 600;
  text-align: center;
  color: #ffffff;
  margin-bottom: 2rem;
  margin-top: 1rem;
}

/* Centraliza o campo de busca */
.search-container {
  width: 100vw;
  max-width: 1100px;
  margin-bottom: 2rem;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.search-group {
  width: 100%;
  display: flex;
  box-shadow: 0 0 0 1px #2e2e2e;
  border-radius: 8px;
  overflow: hidden;
}

.search-input {
  flex: 1;
  padding: 1.2rem;
  margin: 1rem;
  font-size: 1.1rem;
  background-color: #2a2a2a;
  color: #ffffff;
  border: none;
  outline: none;
}

.search-input::placeholder {
  color: #888888;
}

.form-select {
  width: 250px;
  background-color: #2a2a2a;
  color: #ffffff;
  border: none;
  padding: 1.2rem;
  font-size: 1.1rem;
  outline: none;
}

.form-control:focus,
.form-select:focus {
  outline: none;
  box-shadow: none;
}

/* Status e resultados */
.alert {
  width: 100%;
  margin: 1rem 0;
  padding: 1rem;
  text-align: center;
  border-radius: 8px;
  font-size: 0.95rem;
}

.results-container {
  width: 100%;
  flex: 1;
  overflow-y: auto;
  margin-top: 1rem;
  padding: 0 1rem;
}

.loading-container {
  display: flex;
  justify-content: center;
  padding: 2rem;
}

.table-responsive {
  width: 100%;
  overflow-x: auto;
  margin-bottom: 2rem;
}

.table {
  width: 100%;
  font-size: 0.95rem;
  margin-top: 1rem;
  background-color: #2b2b2b;
  color: #ffffff;
  border-collapse: collapse;
  border-radius: 8px;
  overflow: hidden;
}

.table th,
.table td {
  padding: 1rem;
  text-align: left;
  border-bottom: 1px solid #444444;
  white-space: nowrap;
}

.table th {
  background-color: #1a1a1a;
  font-weight: 600;
}

.table-striped tbody tr:nth-of-type(odd) {
  background-color: #242424;
}

.table-hover tbody tr:hover {
  background-color: #3a3a3a;
}

.results-count {
  margin-top: 1rem;
  text-align: right;
  color: #aaa;
  font-size: 0.9rem;
}

.results-count-above {
  width: 100%;
  text-align: center;
  color: #888888;
  font-size: 0.85rem;
  margin-top: 0.5rem;
  font-style: italic;
}

/* Responsividade */
@media (max-width: 1200px) {
  .content-wrapper {
    padding: 1.5rem;
  }
  
  .table {
    font-size: 0.9rem;
  }
  
  .table th,
  .table td {
    padding: 0.8rem;
  }
}

@media (max-width: 100%) {
  .content-wrapper {
    padding: 1rem;
  }
  
  .title {
    font-size: 1.8rem;
  }
  
  .search-container {
    max-width: 100%;
    padding: 0 1rem;
  }
  
  .search-input,
  .form-select {
    padding: 1rem;
    font-size: 1rem;
  }
  
  .form-select {
    width: 200px;
  }
  
  .table {
    font-size: 0.85rem;
  }
}

.representante {
  min-width: 150px;
}

/* Ajustando a largura do container para acomodar mais colunas */
.content-wrapper {
  width: 100%;
  max-width: 1200px;
  background-color: #1e1e1e;
  border-radius: 12px;
  padding: 2.5rem;
  box-shadow: 0 0 12px rgba(0, 0, 0, 0.5);
  display: flex;
  flex-direction: column;
  align-items: center;
}

/* Ajustando a tabela para melhor visualização */
.table {
  width: 100%;
  font-size: 0.9rem;
  margin-top: 1rem;
  background-color: #2b2b2b;
  color: #ffffff;
  border-collapse: collapse;
  border-radius: 8px;
  overflow: hidden;
}

.table th,
.table td {
  padding: 0.8rem;
  text-align: left;
  border-bottom: 1px solid #444444;
  white-space: nowrap;
}

/* Ajustando as larguras mínimas das colunas */
.razao-social {
  min-width: 200px;
}

.nome-fantasia {
  min-width: 180px;
}

.cnpj {
  min-width: 140px;
}

.modalidade {
  min-width: 150px;
}

.localizacao {
  min-width: 100px;
}

.telefone {
  min-width: 120px;
}
</style>
