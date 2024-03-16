# Play It: Discover Musical Instruments

## Project Description

"Play It" is a revolutionary application that blends the innovative capabilities of Claude 3's AI with an intuitive, user-friendly interface. This unique platform invites users of all ages to dive into the world of musical instruments. It enables exploration, learning, and engaging in rich educational conversations powered by visual content.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

Before running "Play It," ensure you have the following installed:
- Python (3.7 or newer)
- Streamlit
- The necessary Python packages: `anthropic`, `base64`, `os`, `dotenv`

### Installation

1. Clone the repository to your local machine.
2. Install the required Python packages by navigating to the project directory and running:
   ```
   pip install streamlit anthropic python-dotenv httpx
   ```
3. Create a `.env` file in the project directory. Inside, add your Anthropic API key:
   ```
   ANTHROPIC_API_KEY=your_api_key_here
   ```
   
### Running the Application

To run "Play It," navigate to the project directory in your terminal and execute:
```
streamlit run playit_streamlit.py
```

## Features

- **Interactive Image Analysis**: Leveraging Claude 3's advanced AI, "Play It" analyzes uploaded images of musical instruments, providing detailed information about their history, usage, and genre.
- **Musical Conversations**: Engage in conversations with Claude 3 about playing techniques, the cultural significance of instruments, or even request pieces of music associated with them.
- **Educational Enrichment**: An invaluable tool for educators and students to supplement music education through interactive discussions and explorations.
- **Exploration for Hobbyists and Musicians**: Whether you're a seasoned musician or a curious newbie, "Play It" opens up a world of musical exploration and discovery.

## Use Cases

- Teachers using the app to enhance classroom music lessons.
- Students exploring musical instruments as part of their studies.
- Musicians and hobbyists discovering new instruments and their stories.

## Contributing

Contributions to "Play It" are welcome! Please read `CONTRIBUTING.md` for details on our code of conduct, and the process for submitting pull requests to us.

