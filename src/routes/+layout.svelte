<script>
  import "../app.css";
  import Header from "$lib/components/Header.svelte";
  import Footer from "$lib/components/Footer.svelte";
 
</script>

<svelte:head>
  <title>Union Zindabad!</title>
</svelte:head>

<Header />

<slot />

<Footer />
