import { Center, Input, Box } from "@chakra-ui/react";
import { login } from "../services/login";
import { Botao } from "./Button";
import { useState, useEffect } from "react";
import { api } from "../api";

export const Card = () => {
  const [email, setEmail] = useState('')

  useEffect(() => {
    const getData = async () => {
      const data = await api
      console.log(data)
    }

    getData()
  })

  const logar = () => {
    alert(email)
  }
  
  return (
    <Box backgroundColor="#FFFFFF" borderRadius="25px" padding="15px">
      <Center>        
        <h1>Faça o login</h1>        
      </Center>
      <Input placeholder="email" value={email} onChange={(event) => setEmail(event.target.value)} margin="10px 0 10px 0" />
      <Input placeholder="password" margin="0 0 10px 0" />
      <Center>
        <Botao onClick={() => login(email)} />
      </Center>
    </Box>
  );
};

export default Card;
