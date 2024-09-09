import { Layout } from "./components/Layout";
import styled from "styled-components";
import { Center, ChakraProvider, Input } from "@chakra-ui/react";

function App() {
  return (
    <ChakraProvider>
      <Center>
        <h1>Faça o login</h1>      
        <Input placeholder="email" />
        <Input placeholder="password" />    
      </Center>          
    </ChakraProvider>
  );
}

export default App;
