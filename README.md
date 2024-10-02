# Generate AI Images using content from Online Articles

This is a simple tool that allows the user the ability to pass in a URL from any web article and generate an image usging the OpenAI API.

The user will need to generate their **OWN** OpenAI key in order to use this tool. 

## Create and Export your API key   
Create an API key in the [dashboard here](https://platform.openai.com/api-keys), which you’ll use to securely access the API. Store the key in a safe location, like a .zshrc file or another text file on your computer. Once you’ve generated an API key, export it as an environment variable in your terminal.

```
export OPENAI_API_KEY="your_api_key_here"
```

## Install OpenAI

To use the OpenAI API in server-side JavaScript environments like Node.js, Deno, or Bun, you can use the official OpenAI SDK for TypeScript and JavaScript. Get started by installing the SDK using npm or your preferred package manager:

```
npm install openai
```