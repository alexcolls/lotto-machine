const basePath = process.cwd();
const { MODE } = require(`${basePath}/constants/blend_mode.js`);
const { NETWORK } = require(`${basePath}/constants/network.js`);

const network = NETWORK.sol;

const namePrefix = "S◎LUCKY";
const description = "SOLucky NFTicket ◎ The Solana onchain-lotto every f*** Friday! A Solana community-based project built-in the Solana blockchain. Are you a Lucky Cat? Visit https://soluckylotto.com to claim your reward.";
const baseUri = "../layers/";

const solanaMetadata = {
  symbol: "S◎LUCKY",
  seller_fee_basis_points: 3000, // Define how much % you want from secondary market sales 1000 = 10%
  external_url: "S◎LUCKY",
  creators: [
    {
      address: "4vL2Fg5rb5DmXdJd2LpWvZxhJz3W6ZeKyzx4rtLypagw",
      share: 100,
    }
  ],
};

const layerConfigurations = [
  {
    growEditionSizeTo: 10,
    layersOrder: [
      { name: "NFTICKET" },
      { name: "LUCKYCAT" },
      { name: "EDITION" },
      { name: "GENERATION" },
      { name: "SUPPLY" },
    ],
  },
];

const extraMetadata = { website: "https://soluckylotto.com", discord: "https://discord.gg/AA4sJBEX", twitter: "https://twitter.com/SOLuckyLotto" };

const rarityDelimiter = "_";

const uniqueDnaTorrance = 100000;

const shuffleLayerConfigurations = false;

const debugLogs = false;

const format = {
  width: 777,
  height: 777,
  smoothing: false,
};

const gif = {
  export: false,
  repeat: 0,
  quality: 100,
  delay: 500,
};

const text = {
  only: false,
  color: "#ffffff",
  size: 20,
  xGap: 40,
  yGap: 40,
  align: "left",
  baseline: "top",
  weight: "regular",
  family: "Courier",
  spacer: " => ",
};

const pixelFormat = {
  ratio: 2 / 128,
};

const background = {
  generate: false,
  brightness: "100%",
  static: false,
  default: "#000000",
};

const preview = {
  thumbPerRow: 5,
  thumbWidth: 50,
  imageRatio: format.height / format.width,
  imageName: "preview.png",
};

const preview_gif = {
  numberOfImages: 5,
  order: "ASC", // ASC, DESC, MIXED
  repeat: 0,
  quality: 100,
  delay: 500,
  imageName: "preview.gif",
};

module.exports = {
  format,
  baseUri,
  description,
  background,
  uniqueDnaTorrance,
  layerConfigurations,
  rarityDelimiter,
  preview,
  shuffleLayerConfigurations,
  debugLogs,
  extraMetadata,
  pixelFormat,
  text,
  namePrefix,
  network,
  solanaMetadata,
  gif,
  preview_gif,
};
