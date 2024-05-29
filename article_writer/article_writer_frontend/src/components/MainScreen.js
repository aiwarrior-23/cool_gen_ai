import React, { useState } from 'react';
import './MainScreen.css';

const MainScreen = () => {
    const [problem, setProblem] = useState('');
    const [data, setData] = useState(null);
    const [error, setError] = useState(null);
    const [loading, setLoading] = useState(false);

    const handleGenerateArticle = () => {
        setLoading(true);
        setError(null);
        fetch('http://localhost:5000/generate_article', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ problem }), // Send the problem statement from the input
        })
            .then((response) => {
                setLoading(false);
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                return response.json();
            })
            .then((data) => setData(data))
            .catch((error) => {
                setLoading(false);
                setError(error.toString());
            });
    };

    const renderContent = (content, level = 1) => {
        return content.map((item, index) => (
            <div key={index} className={`level-${level}`} style={{ textAlign: 'left' }}>
                {item.Heading && <h2 style={{ fontSize: `${2 - level * 0.2}em` }}>{item.Heading}</h2>}
                {item.Content && <p>{item.Content}</p>}
                {item.List && (
                    <ul>
                        {item.List.map((listItem, i) => (
                            <li key={i}>{listItem.ListItem}</li>
                        ))}
                    </ul>
                )}
                {item.Code && item.Code.map((codeItem, i) => (
                    <div key={i} className="code-block">
                        {codeItem.CodeBlock && <pre>{codeItem.CodeBlock}</pre>}
                        {codeItem.Content && <p>{codeItem.Content}</p>}
                    </div>
                ))}
                {item.Examples && item.Examples.map((example, i) => (
                    <div key={i} className="example-block">
                        {example.Content && <p>{example.Content}</p>}
                        {example.Code && example.Code.map((codeItem, j) => (
                            <div key={j} className="code-block">
                                {codeItem.CodeBlock && <pre>{codeItem.CodeBlock}</pre>}
                            </div>
                        ))}
                    </div>
                ))}
                {item.Link && <p><a href={item.Link} target="_blank" rel="noopener noreferrer">{item.Link}</a></p>}
            </div>
        ));
    };

    return (
        <div className="main-screen">
            <textarea
                value={problem}
                onChange={(e) => setProblem(e.target.value)}
                placeholder="Write your problem statement here..."
                rows="4"
            />
            <button onClick={handleGenerateArticle} disabled={loading}>
                {loading ? 'Generating...' : 'Generate Article'}
            </button>
            {error && <div className="error">Error: {error}</div>}
            {data && (
                <div className="article-content">
                    <h1 style={{ fontWeight: 'bolder', fontSize: '40px' }}>{data.Title}</h1>
                    {renderContent(data.Body)}
                </div>
            )}
        </div>
    );
};

export default MainScreen;