const inputField = document.getElementById("question");
const outputContainer = document.getElementById("chat-output");

function appendUserMessage(text) {
  const message = document.createElement("div");
  message.className = "chat-message user-message";
  message.textContent = text;
  outputContainer.appendChild(message);
  outputContainer.scrollTop = outputContainer.scrollHeight;
}

function appendAIMessage(text, isLoading = false) {
  const message = document.createElement("div");
  message.className = "chat-message ai-message";
  message.textContent = isLoading ? text : "";
  outputContainer.appendChild(message);
  outputContainer.scrollTop = outputContainer.scrollHeight;
  return message;
}

function typeWriterEffect(element, text, speed = 20) {
  let i = 0;
  function type() {
    if (i < text.length) {
      element.textContent += text.charAt(i);
      i++;
      setTimeout(type, speed);
    }
  }
  type();
}

inputField.addEventListener("keydown", function (e) {
  if (e.key === "Enter" && !e.shiftKey) {
    e.preventDefault();
    const question = inputField.value.trim();
    if (!question) return;

    appendUserMessage(question);
    const aiMsg = appendAIMessage("Thinking...", true);

    chrome.tabs.query({ active: true, currentWindow: true }, async (tabs) => {
      const url = tabs[0].url;
      try {
        const response = await fetch("http://localhost:8000/scrape", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ url: url, Question: question }),
        });
        const data = await response.json();
        if (data.answer) {
          aiMsg.textContent = "";
          typeWriterEffect(aiMsg, data.answer);
        } else {
          aiMsg.textContent = "No answer found.";
        }
      } catch (err) {
        aiMsg.textContent = "Error: Could not fetch.";
      }
    });

    inputField.value = "";
  }
});
