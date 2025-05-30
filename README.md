# Union Zindabad! 

A digital exhibit exploring South Asian Canadian Labour History in British Columbia.

## About the Project

**Union Zindabad!** is a comprehensive digital exhibit that traces the long and complex relationship between South Asian Canadians and the labour movement in British Columbia. From early exclusionary practices to the recognition that racism is a tool used by bosses to divide workers, this exhibit showcases the tenacity and strength of the South Asian Canadian community.

The title "Zindabad" (meaning "Long live" in Punjabi, Hindi, Urdu, Odia and Bengali) has been heard in cries of "Farmworkers Zindabad!" at massive protest rallies in recent decades, encapsulating the spirit of South Asian Canadian labour activism.

## Project Partners

This project is a collaboration between:

- **[South Asian Studies Institute](http://www.ufv.ca/sasi)** (University of the Fraser Valley)
- **[BC Labour Heritage Centre](https://www.labourheritagecentre.ca/)**
- **[University of the Fraser Valley](http://www.ufv.ca/)**
- **[Province of British Columbia](https://www2.gov.bc.ca/)**

Supported by a $1.14 million contribution from the Province of BC as part of the [South Asian Canadian Legacy Project](https://www.ufv.ca/sasi/south-asian-canadian-legacy-project/).

## Content Coverage

The exhibit covers key themes including:

- **Early Migration** - The White Man's Province, 1907 racist riots, and early work experiences
- **Finding Work** - Migration patterns, Golden Sikhs, Tod Inlet, Gurdwaras and work, bunkhouse life
- **Revolutionaries** - The Ghadar movement, Industrial Workers of the World, key figures like Husain Rahim
- **Union Organization** - One Big Union, Fraser Mills Strike 1931, CCF and NDP connections
- **International Woodworkers of America (IWA)** - Key figures like Darshan Singh Sangha, franchise support, bargaining victories
- **Women Workers** - Women's activism, formal economy entry, union participation
- **New Labour Alliances** - Fighting racism, solidarity movements
- **Canadian Farmworkers Union** - Working conditions, organizing, strikes, cultural movements
- **New Economies** - Taxi industry, longshoring, trucking

## Technology Stack

Built with:
- **SvelteKit** - Full-stack web framework
- **TypeScript** - Type-safe development
- **Tailwind CSS** - Utility-first styling
- **Vite** - Build tool and development server
- **Static Site Generation** - Pre-rendered for optimal performance

## Development

Install dependencies:
```bash
npm install
# or
pnpm install
```

Start the development server:
```bash
npm run dev
# or start the server and open the app in a new browser tab
npm run dev -- --open
```

## Building

Create a production build:
```bash
npm run build
```

Preview the production build:
```bash
npm run preview
```

## Deployment

The project is configured for static site deployment with the following setup:
- Uses `@sveltejs/adapter-static` for static site generation
- Base path configured for `/exhibits/union-zindabad-exhibit`
- Pre-renders all exhibit pages for optimal performance
- Deployment script included for GitHub Pages deployment

Deploy using the included script:
```bash
./deploy.sh
```

## Project Structure

```
src/
├── lib/
│   ├── components/          # Reusable Svelte components
│   │   ├── Header.svelte   # Site header
│   │   ├── Footer.svelte   # Site footer
│   │   ├── Navigation.svelte
│   │   └── NextPrevNav.svelte
│   └── utils/
│       └── contents.ts      # Exhibit content data
├── routes/
│   ├── +layout.svelte      # Global layout
│   ├── +page.svelte        # Home page
│   └── [id]/
│       ├── +page.svelte    # Dynamic exhibit pages
│       └── +page.ts        # Page configuration
└── app.html                # HTML template
```

## Contributing

This exhibit is part of ongoing research into South Asian Canadian labour history. For inquiries about the content or to contribute historical materials, please contact the South Asian Studies Institute at the University of the Fraser Valley.

## License

Content and research materials are part of the South Asian Canadian Legacy Project. Please refer to the project partners for usage and attribution guidelines.
