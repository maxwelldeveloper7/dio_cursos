import { Button } from "@chakra-ui/react";
import { MouseEventHandler } from "react";

interface IBotao{
    onClick: MouseEventHandler;
}

export const Botao = ({ onClick }: IBotao ) => {
  return(
    <Button colorScheme="teal" onClick={onClick} size='sm' width='100%' marginTop='5px'>Entrar</Button>
  )
};

export default Botao;