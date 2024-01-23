const {Configuration, OpenAIApi} = require("openai");

module.exports = class openai{
    static configuration(){
        const openai = new OpenAI({
          apiKey: process.env.OPENAI_API_KEY,
        });
        return openai;
    }

    static textCompletion({prompt}){
        return{
            model: "gpt-3.5-turbo-instruct",
            prompt: `${prompt}`,
            temperature: 0,
            max_tokens: 256,
            top_p: 1,
            frequency_penalty: 0,
            presence_penalty: 0,
        }
    }
}
