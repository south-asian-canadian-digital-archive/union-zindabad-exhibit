import adapter from '@sveltejs/adapter-static';
import { vitePreprocess } from '@sveltejs/vite-plugin-svelte';

/** @type {import('@sveltejs/kit').Config} */
const config = {
	// Consult https://kit.svelte.dev/docs/integrations#preprocessors
	// for more information about preprocessors
	preprocess: vitePreprocess(),

	kit: {
		// adapter-auto only supports some environments, see https://kit.svelte.dev/docs/adapter-auto for a list.
		// If your environment is not supported or you settled on a specific environment, switch out the adapter.
		// See https://kit.svelte.dev/docs/adapters for more information about adapters.
		adapter: adapter(
			{
				pages: 'build',
				assets: 'build',
				fallback: null,
				precompress: false,
				strict: true,

			}
		),

		prerender: {
			handleMissingId: 'warn',	
			entries: ["/cover", "/south-asian-canadian-labour-history-project", "/preface", "/truth", "/introduction", "/the-white-mans-province", "/the-1907-racist-riots", "/finding-work", "/migration", "/golden-sikhs", "/tod-inlet", "/gurdwaras-and-work", "/bunkhouse-life", "/wood-fuel", "/labour-contractors", "/wages-and-race", "/revolutionaries", "/the-ghadar-movement", "/industrial-workers-of-the-world", "/husain-rahim", "/searching-for-working-class-unity", "/one-big-union", "/fraser-mills-strike-1931", "/upward-mobility-or-union-membership", "/the-ccf-and-ndp", "/international-woodworkers-of-america-iwa", "/darshan-singh-sangha", "/supporting-the-franchise", "/colonialism-fascism-and-racism", "/winning-at-the-bargaining-table", "/proud-iwa-members", "/women", "/women-workers-and-activism", "/entering-the-formal-economy", "/union-activism", "/new-labour-alliances", "/fighting-racism", "/solidarity-movement", "/canadian-farmworkers-union", "/working-conditions", "/farmworkers-organizing-committee-and-canadian-farmworkers-union", "/organizing-and-strikes", "/a-social-movement", "/culture", "/racism-and-backlash", "/achievements-and-legacies", "/new-economies", "/taxis", "/longshoring", "/trucking", "/conclusion", "/appendix", "/bibliography"],
			
		}
	},

};

export default config;
