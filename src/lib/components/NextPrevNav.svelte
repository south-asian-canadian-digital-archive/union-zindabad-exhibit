<script lang="ts">
  import { goto } from "$app/navigation";
  import { direction } from "$lib/utils/nav.store";

  export let nextPage: string | null;
  export let prevPage: string | null;
</script>

<div class="w-full flex justify-between">
  {#if prevPage !== null}
    <button
      class="group"
      on:click={() => {
        $direction = -1;
        goto(`../${prevPage}`, { noScroll: true });
      }}
    >
      <span
        class="fa fa-arrow-left group-hover:-translate-x-2 transition-all ease-in-out duration-300"
      ></span>
      Prev
    </button>
  {:else}
    <div />
  {/if}

  {#if nextPage !== null}
    <button
      hidden={nextPage === null}
      class="group"
      on:click={() => {
        $direction = 1;
        goto(`../${nextPage}`, { noScroll: true });
      }}
    >
      Next
      <span
        class="fa fa-arrow-right group-hover:translate-x-2 transition-all ease-in-out duration-300"
      ></span>
    </button>
  {:else}
    <div />
  {/if}
</div>
