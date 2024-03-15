<script>
  import { goto } from "$app/navigation";
  import { onMount } from "svelte";

  const logos = [
    {
      name: "South Asian Studies Institute",
      link: "http://www.ufv.ca/sasi",
      image:
        "https://sacda.ca//themes/sacda/assets/pawtucket/graphics/footer/sasi.svg",
    },
    {
      name: "University of the Fraser Valley",
      link: "http://www.ufv.ca/",
      image:
        "https://sacda.ca//themes/sacda/assets/pawtucket/graphics/footer/ufv.svg",
    },
    {
      name: "BC Labour Heritage Centre",
      link: "https://www.labourheritagecentre.ca/",
      image: "/images/preface_img_0.png",
    },
  ];

  onMount(() => {
    // goto("./cover");
  });
</script>

<div class="bg-[url(/cover_bg.jpg)] p-6 md:p-20 lg:p-20 bg-cover h-full">
  <div
    class="flex flex-col lg:flex-row md:flex-row overflow-clip justify-center"
  >
    <div class="flex flex-col lg:gap-16 md:gap-16 z-10 md:-mr-[10vw] lg:-mr-[10vw]">
      <div
        class="lg:text-[6vw] md:text-[6vw] text-5xl z-10 text-shadow font-lexend-peta text-white pt-10"
      >
        <p>Union</p>
        <p class="">Zindabad</p>
      </div>

      <div class="lg:hidden md:hidden w-[80vw] -my-4 self-end">
        <img src="/cover_right.png" alt="" class="" />
      </div>

      <div class="bg-black rounded-lg w-fit md:ml-[10vw] lg:ml-[10vw] z-10">
        <button
          class="rounded-lg p-2 px-6 md:text-lg lg:text-lg font-bold bg-white border border-black text-[#000000D1] -translate-y-1 translate-x-1 hover:-translate-y-2 hover:translate-x-2 transition-all duration-500 ease-in-out"
          on:click={() => {
            goto("/cover");
          }}>Read Book</button
        >
      </div>

      <div
        class="font-bold lg:text-base md:text-base mt-8 lg:mt-0 md:mt-0 text-xs text-left text-white md:max-w-[25vw] lg:max-w-[25vw] flex flex-col gap-4"
      >
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
      </div>
    </div>

    <div class="h-full">
      <div
        class="relative h-fit min-w-[55vw] hidden lg:block md:block rounded-[20px] object-cover"
      >
        <img src="/cover_right.png" alt="" class="w-full" />
        <p
          class="absolute text-[#f5f5f5] text-right text-xs font-bold bottom-4 right-4 max-w-[70%]"
        >
          On March 20, 1943 District union official Nigel Morgan reported that
          the 'East Indians' at the Youbou Mill were 100% unionized. Kaatza
          Station Museum & Archives, N01603, IWA Local 1-80, Wilmer Gold Photo
          Collection, ©United Steelworkers Local 1-1937.
        </p>
      </div>

      <div class="flex w-full justify-evenly lg:pt-14 md:pt-14 py-8 items-center h-full">
        {#each logos as logo}
          <a href={logo.link} target="_blank">
            <img
              src={logo.image}
              alt={logo.name}
              class="lg:w-[12vw] md:w-[12vw] w-[25vw] h-auto object-contain"
            />
          </a>
        {/each}
      </div>
    </div>
  </div>
</div>

<style type="postcss">
  p a {
    @apply border-b border-b-white transition-all ease-in-out duration-200 hover:border-b-transparent;
  }
  .text-shadow {
    text-shadow: -12px 11px 4px rgba(0, 0, 0, 0.25);
    /* font-family: 'Lexend Peta', sans-serif !important; */
  }
</style>
