<script>
  import { goto } from "$app/navigation";
  import { onMount } from "svelte";

  onMount(() => {
    // goto("./cover");
  });
</script>

<div class="flex justify-evenly gap-10 p-20">
  <div class="w-1/2 flex flex-col gap-4">
    <h1 class="text-5xl">Union Zindabad</h1>
    <p>
      View Exhibit of South Asian Canadian Labour History in British Columbia
    </p>
    <p>
      South Asian Studies Institute; University of the Fraser Valley — South
      Asian Studies Institute; and BC Labour Heritage Centre
    </p>

    <p>
      Explore the South Asian Canadian Digital Archive
      <a href="https://sacda.ca">
        View all SACDA archival collections and exhibits (www.sacda.ca)
      </a>
    </p>

    <p>
      Find labour history archival images View the full <a
        href="https://sacda.ca/index.php/Detail/collections/746"
      >
        South Asian Canadian Labour History archival image collection</a
      >
    </p>

    <p>Supported by the Province of British Columbia</p>

    <div class="w-full flex justify-center">
      <button
        class="uppercase px-10 py-2 border border-black rounded-lg hover:translate-x-1 hover:-translate-y-1 transition-all duration-500"
        on:click={() => goto("./cover")}>Read book</button
      >
    </div>
  </div>

  <img
    class="w-1/2 rounded-lg"
    src="https://pressbooks.pub/app/uploads/sites/4310/2020/07/SM_BANNER_IMAGE-LABOUR-HERITAGE.png"
    alt=""
  />
</div>

<style type="postcss">
  a {
    @apply border-b border-b-black transition-all ease-in-out duration-200 hover:border-b-transparent;
  }

  p {
    @apply text-lg;
  }
</style>
