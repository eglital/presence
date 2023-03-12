import { useState, useEffect } from "react";

function GithubIssues() {
  const [issues, setIssues] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  useEffect(() => {
    setLoading(true);
    fetch(
      "http://localhost:8000/api/github-issues/?owner=Microsoft&name=vscode"
    )
      .then((response) => response.json())
      .then((data) => {
        setIssues(data);
        setLoading(false);
      })
      .catch((error) => {
        setError(error);
        setLoading(false);
      });
  }, []);

  if (loading) {
    return <div>Loading...</div>;
  }

  if (error) {
    return <div>Error: {error.message}</div>;
  }

  return (
    <div>
      <h1>Github issues</h1>
      <div className="container">
        {issues.map((issue) => (
          <div key={issue.number} className="issueBox">
            <a href={issue.url} target="_blank" rel="noopener noreferrer">
              {issue.title}
            </a>
            <p>Number: {issue.number}</p>
            <p>
              Author:{" "}
              <a
                href={issue.author_url}
                target="_blank"
                rel="noopener noreferrer"
              >
                {issue.author_name}
              </a>
            </p>
            <p>Created At: {issue.created_at}</p>
          </div>
        ))}
      </div>
    </div>
  );
}

export default GithubIssues;
