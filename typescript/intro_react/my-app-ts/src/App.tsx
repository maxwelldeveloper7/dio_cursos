import { Layout } from "./components/Layout";
import styled from "styled-components";

const Box = styled.div`
  background-color: orange;
  border-radius: 25px;
  padding: 15px;
`;

function App() {
  return (
    <Layout>
      <Box>
        <h1>Faça o login</h1>
      </Box>
      <label htmlFor='emailInput'>
        Email:
      </label>
      <input id='emailInput' type="email"/>

      <label htmlFor='passwordInput'>
        Senha:
      </label>
      <input id='passwordInput' type="password"/>
      <button>
        Entrar
      </button>
    </Layout>
  );
}

export default App;
