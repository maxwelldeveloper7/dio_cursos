import { Center, Input, Box, Heading } from "@chakra-ui/react";
import { login } from "../services/login";
import { Botao } from "./Button";
import { useState } from "react";

export const Card = () => {
  const [email, setEmail] = useState('')

  const logar = () => {
    alert(email)
  }
  
  return (
    <Box backgroundColor="#FFFFFF" borderRadius="25px" padding="15px">
      <Center>
        <Heading as="h2" size="md">
          Faça o login
        </Heading>
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
