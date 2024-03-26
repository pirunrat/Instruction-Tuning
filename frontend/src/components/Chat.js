import React, { useState } from 'react';
import './Chat.css';
import axios from 'axios';

const Chat = () => {
    const [instruction, setInstruction] = useState('');
    const [promptInput, setPromptInput] = useState('');
    const [inputWord, setInputWord] = useState('');
    const [response, setResponse] = useState('');

    const handleAPIRequest = async (e) => {
        e.preventDefault();

        try {
            const response = await axios.post('http://localhost:5000/question', {
                "instruction": instruction,
                "promptInput": promptInput,
                "question": inputWord
            });

            if (response && response.data) {
                setResponse(response.data);
                console.log(response.data.answer);
            }
        } catch (error) {
            console.error('Error making request:', error);
        }
    };

    return (
        <div className="chat-container">
            {/* <form onSubmit={handleAPIRequest}>
                <label>
                    Enter a word:
                    <input
                        type="text"
                        value={inputWord}
                        onChange={(e) => setInputWord(e.target.value)}
                        placeholder="Type a word..."
                    />
                </label>
                <button type="submit">Submit</button>
            </form>

            {response && (
                <div className="response-container">
                    <p>Answer:</p>
                    <p>{response.answer}</p>
                </div>
            )} */}

            <div className="query_box">
                <h3 className="web_title">Text Generator</h3>
                <form onSubmit={handleAPIRequest}>
                    <label htmlFor="Instruction">Instruction:</label>
                    <br />
                    <div className="prompt_inner">
                        <input
                            type="text"
                            name="instruction"
                            id="fill_in"
                            value={instruction}
                            onChange={(e) => setInstruction(e.target.value)}
                            required
                        />
                    </div>
                    <label htmlFor="Input">Input:</label>
                    <br />
                    <div className="prompt_inner">
                        <input
                            type="text"
                            name="prompt_input"
                            id="fill_in"
                            value={promptInput}
                            onChange={(e) => setPromptInput(e.target.value)}
                        />
                    </div>
                    <input id="submit" type="submit" value="Submit" />
                </form>
            </div>

            {response && (
                <div className="response-container">
                    <p>Answer:</p>
                    <p>{response.answer}</p> {/* This line needs adjustment */}
                </div>
            )}
        </div>
    );
};

export default Chat;
